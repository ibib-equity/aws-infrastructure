"""
This lambda function handles collibra glue integration
"""
import io
import json
import os
import uuid
import boto3
import logging
import requests

from shared import get_auth_token, import_sync

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, _):
    """
    Here we parse the triggering event and pass data from function to function.
    This function should be as clean as possible with any complex logic being handled in other functions.
    """
    logger.info(event)

    microsoft_credentials = {
        "client_id": os.environ["azure_client_id"],
        "client_secret": os.environ["azure_client_secret"],
    }

    microsoft_auth_url = os.environ["microsoft_auth_url"]

    auth_token = get_auth_token(microsoft_auth_url, microsoft_credentials)
    asset_reference_ids = construct_asset_reference_ids()
    relationship_reference_ids = construct_relationship_reference_ids()
    schemas_community_id, databases_domain_id, collibra_api_endpoints = construct_collibra_pieces()

    if event["detail"]["eventName"] == "CreateTable" or event["detail"]["eventName"] == "UpdateTable":
        database = event["detail"]["requestParameters"]["databaseName"]
        json_file, sync_id_value = construct_dictionary(event)

        import_sync(collibra_api_endpoints, json_file, sync_id_value, auth_token)

        asset_id = find_domain(event["detail"]["requestParameters"]["databaseName"],
                               asset_reference_ids["data_dictionary"], auth_token, collibra_api_endpoints)

        database_id = find_database_id(database, asset_reference_ids, collibra_api_endpoints, auth_token)

        fab_asset_id = find_fab_asset(asset_reference_ids, collibra_api_endpoints, auth_token)

        database_fab_relations_results = relate_database_to_fab_asset(fab_asset_id, database_id,
                                                                      relationship_reference_ids,
                                                                      collibra_api_endpoints,
                                                                      auth_token)

        logger.info(database_fab_relations_results)
        import_sync_validation_id = get_import_sync_workflow_id(auth_token, collibra_api_endpoints)

        import_sync_results = start_import_sync_workflow(collibra_api_endpoints, auth_token, import_sync_validation_id,
                                                         asset_id)

        logger.info(import_sync_results)

    elif event["detail"]["eventName"] == "DeleteDatabase":
        asset_id = find_domain(event["detail"]["requestParameters"]["name"], asset_reference_ids["data_dictionary"],
                               auth_token, collibra_api_endpoints)
        delete_database_asset(asset_id, auth_token, collibra_api_endpoints)

    elif event["detail"]["eventName"] == "DeleteTable":
        asset_id = find_asset(asset_reference_ids, event["detail"]["requestParameters"]["name"],
                              asset_reference_ids["table"], collibra_api_endpoints, auth_token)
        logger.info('DELETING COLUMNS')
        del_columns(asset_id, relationship_reference_ids, collibra_api_endpoints, auth_token)
        logger.info('DELETING TABLE')
        delete_table_asset(collibra_api_endpoints, asset_id, auth_token)


def get_import_sync_workflow_id(auth_token, collibra_api_endpoints):
    """
    Here we import the sync workflow id from collibra
    """
    headers = {
        'Authorization': auth_token
    }

    payload = {
        'name': "Import Sync Validation"
    }
    url = collibra_api_endpoints["workflow_definition"]

    results = requests.get(url, headers=headers, params=payload)

    import_sync_validation_id = results.json()["results"][0]["id"]
    logger.info("import sync validation id: " + import_sync_validation_id)

    return import_sync_validation_id


def start_import_sync_workflow(collibra_api_endpoints, auth_token, import_sync_validation_id, asset_id):
    """
    Here we start the sync workflow with collibra
    """
    url = collibra_api_endpoints["workflow_start"]
    headers = {
        'Authorization': auth_token
    }

    payload = {
        "workflowDefinitionId": import_sync_validation_id,
        "businessItemIds": [asset_id],
        "businessItemType": "DOMAIN"
    }

    response = requests.post(url, headers=headers, json=payload)
    logger.info('workflow started' + str(response.json()))

    return response.json()


def sync_id_find(database, table):
    """
    Here we connect to dynamodb and find the sync id
    """
    dynamodb = boto3.client('dynamodb')
    dynamodb_table = os.environ["dynamodb_table"]
    database_name_db = database
    table_name_db = table
    try:
        response = dynamodb.get_item(
            TableName=dynamodb_table,
            Key={
                'database-name': {'S': database_name_db},
                'table-name': {'S': table_name_db}
            }
        )
        if 'Item' in response:
            item = response['Item']
            database_value = item.get('database-name', {}).get('S', '')
            table_value = item.get('table-name', {}).get('S', '')
            sync_id_value = item.get('sync-id', {}).get('S', '')
            logger.info(f'database_value Value: {database_value}, table_value Value: {table_value}, '
                        f'sync_id_value Value: {sync_id_value}')
            return sync_id_value

        else:
            logger.info('item not found in dynamodb, creating new record')
            random_uuid = uuid.uuid4()
            sync_id_value = str(random_uuid)
            item_to_add = {
                'database-name': {'S': database_name_db},
                'table-name': {'S': table_name_db},
                'sync-id': {'S': sync_id_value}
            }
            dynamodb.put_item(
                TableName=dynamodb_table,
                Item=item_to_add
            )
            logger.info('item added to dynamodb')
            return sync_id_value

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }


def delete_table_asset(collibra_api_endpoints, asset_id, auth_token):
    """
    Here we delete table assets as needed.
    """
    response = requests.delete(
        collibra_api_endpoints["assets"] + "/" + asset_id,
        headers={'Authorization': auth_token},
    )

    logger.info("Asset Delete Results: " + str(response))
    return response


def del_columns(asset_id, relationship_reference_ids, collibra_api_endpoints, auth_token):
    """
    Here we delete table columns as needed.
    """
    payload = {
        "targetId": asset_id,
        "relationTypeId": relationship_reference_ids["column_to_table"],
    }

    results = requests.get(
        collibra_api_endpoints["relations"],
        headers={'Authorization': auth_token},
        params=payload,
    )

    logger.info("Column Relation results: " + str(results.json()))
    column_ids = []
    for result in results.json()["results"]:
        column_ids.append(result["source"]["id"])

    column_relation_ids = []
    for result in results.json()["results"]:
        column_relation_ids.append(result["id"])

    delete_results = requests.delete(
        collibra_api_endpoints["assets_bulk"],
        headers={'Authorization': auth_token},
        json=column_ids,
    )
    logger.info("Column Delete results" + str(delete_results.status_code))

    column_relations_results = requests.delete(
        collibra_api_endpoints["relations_bulk"],
        headers={'Authorization': auth_token},
        json=column_relation_ids,
    )
    logger.info("Delete relations results:")
    logger.info(column_relations_results.status_code)


def delete_database_asset(asset_id, auth_token, collibra_api_endpoints):
    """
    Here we delete database details as needed.
    """
    payload = [asset_id]
    r = requests.post(
        collibra_api_endpoints["domains"] + "/removalJobs",
        headers={'Authorization': auth_token},
        json=payload
    )

    logger.info("Asset Delete Results")
    logger.info(r.json())


def find_asset(asset_reference_ids, asset_name, type_id, collibra_api_endpoints, auth_token):
    """
    Here we find the assets in Collibra.
    """
    if type_id == asset_reference_ids["schema"]:
        payload = {
            "name": asset_name + '.' + asset_name,
            "typeId": type_id,
            "nameMatchMode": "EXACT"
        }
    else:
        payload = {
            "name": asset_name,
            "typeId": type_id,
            "nameMatchMode": "EXACT"
        }
    logger.info('Asset search result: ')
    logger.info(payload)

    results = requests.get(
        collibra_api_endpoints["assets"],
        headers={'Authorization': auth_token},
        params=payload,
    )
    return results.json()["results"][0]


def find_domain(asset_name, type_id, auth_token, collibra_api_endpoints):
    """
    Here we find the domain details in Collibra.
    """
    payload = {
        "name": asset_name,
        "typeId": type_id,
        "nameMatchMode": "EXACT",
    }
    logger.info('Asset search result: ')
    logger.info(payload)

    results = requests.get(
        collibra_api_endpoints["domains"],
        headers={'Authorization': auth_token},
        params=payload,
    )
    return results.json()["results"][0]["id"]


def find_database_id(database, asset_reference_ids, collibra_api_endpoints, auth_token):
    """
    Here we find the database id from collibra.
    """
    payload = {
        "name": database,
        "typeId": asset_reference_ids["database"],
        "nameMatchMode": "EXACT"
    }
    logger.info('database search result: ' + str(payload))

    results = requests.get(
        collibra_api_endpoints["assets"],
        headers={'Authorization': auth_token},
        params=payload,
    )

    return results.json()["results"][0]["id"]


def find_fab_asset(asset_reference_ids, collibra_api_endpoints, auth_token):
    """
    Here we find the fab asset details from collibra.
    """
    payload = {
        "name": "Fabric Access Bridge ( FAB )",
        "typeId": asset_reference_ids["system"],
        "nameMatchMode": "EXACT"
    }
    logger.info('fab asset search result: ' + str(payload))

    results = requests.get(
        collibra_api_endpoints["assets"],
        headers={'Authorization': auth_token},
        params=payload,
    )
    return results.json()["results"][0]["id"]


def relate_database_to_fab_asset(fab_asset_id, database_id, relationship_reference_ids, collibra_api_endpoints,
                                 auth_token):
    """
    Here we correlate the database to the fab asset
    """
    payload = [
        {
            "sourceId": fab_asset_id,
            "targetId": database_id,
            "typeId": relationship_reference_ids["database_to_system"],
        }
    ]
    logger.info("Database schema relations payload: " + str(payload))

    database_fab_relations_results = requests.post(
        collibra_api_endpoints["relations_bulk"],
        headers={'Authorization': auth_token},
        json=payload,
    )

    return database_fab_relations_results


def construct_asset_reference_ids():
    """
    Here we construct the asset reference ids
    """
    asset_reference_ids = {
        "schema": "00000000-0000-0000-0001-000400000002",
        "table": "00000000-0000-0000-0000-000000031007",
        "column": "00000000-0000-0000-0000-000000031008",
        "data_dictionary": "00000000-0000-0000-0000-000000030011",
        "database": "00000000-0000-0000-0000-000000031006",
        "system": "00000000-0000-0000-0000-000000031302"
    }

    return asset_reference_ids


def construct_relationship_reference_ids():
    """
    Here we construct the relationship reference ids
    """
    relationship_reference_ids = {
        "table_to_database": "00000000-0000-0000-0000-000000007043",
        "column_to_table": "00000000-0000-0000-0000-000000007042",
        "database_to_schema": "00000000-0000-0000-0000-000000007024",
        "database_to_system": "00000000-0000-0000-0000-000000007054"
    }

    return relationship_reference_ids


def construct_collibra_pieces():
    """
    Here we construct the collibra pieces
    """
    schemas_community_id = os.environ['schemas_community_id']
    databases_domain_id = os.environ['databases_domain_id']
    collibra_url = os.environ['collibra_url']

    collibra_api_endpoints = {
        "assets": collibra_url + "/assets",
        "assets_bulk": collibra_url + "/assets/bulk",
        "relations_bulk": collibra_url + "/relations/bulk",
        "relations": collibra_url + "/relations",
        "domains": collibra_url + "/domains",
        "attributes": collibra_url + "/attributes",
        "import_sync": collibra_url + "/import/synchronize/",
        "workflow_start": collibra_url + "/workflowInstances",
        "workflow_definition": collibra_url + "/workflowDefinitions"
    }

    return schemas_community_id, databases_domain_id, collibra_api_endpoints


def construct_dictionary(event):
    """
    Here we construct the dictionary
    """
    database = event["detail"]["requestParameters"]["databaseName"]
    schema = database + "." + database
    columns = event["detail"]["requestParameters"]["tableInput"]["storageDescriptor"]["columns"]
    physical_data_dictionary = database
    table = event["detail"]["requestParameters"]["tableInput"]["name"]

    sync_id_value = sync_id_find(database, table)

    logger.info('sync_id_value:' + str(sync_id_value))

    dictionary = [
        {
            "resourceType": "Asset",
            "identifier": {
                "name": database,
                "domain": {
                    "name": "Databases",
                    "community": {
                        "name": "Business Analysts Community"
                    }
                }
            },
            "type": {
                "name": "Database"
            },
            "relations": {
                "00000000-0000-0000-0000-000000007024:TARGET": [
                    {
                        "name": schema,
                        "domain": {
                            "name": physical_data_dictionary,
                            "community": {
                                "name": "Schemas"
                            }
                        }
                    }
                ]
            }
        },
        {
            "resourceType": "Domain",
            "identifier": {
                "name": physical_data_dictionary,
                "community": {
                    "name": "Schemas"
                }
            },
            "type": {
                "name": "Physical Data Dictionary"
            }
        },
        {
            "resourceType": "Asset",
            "identifier": {
                "name": schema,
                "domain": {
                    "name": physical_data_dictionary,
                    "community": {
                        "name": "Schemas"
                    }
                }
            },
            "type": {
                "name": "Schema"
            },
            "relations": {
                "00000000-0000-0000-0000-000000007043:TARGET": [
                    {
                        "name": table,
                        "domain": {
                            "name": physical_data_dictionary,
                            "community": {
                                "name": "Schemas"
                            }
                        }
                    }
                ]
            },
            "relations": {
                "00000000-0000-0000-0000-000000007024:SOURCE": [
                    {
                        "name": database,
                        "domain": {
                            "name": "Databases",
                            "community": {
                                "name": "Business Analysts Community"
                            }
                        }
                    }
                ]
            }
        },
        {
            "resourceType": "Asset",
            "identifier": {
                "name": table,
                "domain": {
                    "name": physical_data_dictionary,
                    "community": {
                        "name": "Schemas"
                    }
                }
            },
            "type": {
                "name": "Table"
            },
            "relations": {
                "00000000-0000-0000-0000-000000007042:SOURCE": [
                    {
                        "name": table + " > " + column["name"],
                        "domain": {
                            "name": physical_data_dictionary,
                            "community": {
                                "name": "Schemas"
                            }
                        }
                    }
                ] for column in columns
            },
            "relations": {
                "00000000-0000-0000-0000-000000007043:SOURCE": [
                    {
                        "name": schema,
                        "domain": {
                            "name": physical_data_dictionary,
                            "community": {
                                "name": "Schemas"
                            }
                        }
                    }
                ]
            }
        },
        [
            {
                "resourceType": "Asset",
                "identifier": {
                    "name": table + " > " + column["name"],
                    "domain": {
                        "name": physical_data_dictionary,
                        "community": {
                            "name": "Schemas"
                        }
                    }
                },
                "type": {
                    "name": "Column"
                },
                "attributes": {
                    "Technical Data Type": [
                        {
                            "value": column["type"].split('<')[0]
                        }
                    ]
                },
                "relations": {
                    "00000000-0000-0000-0000-000000007042:TARGET": [
                        {
                            "name": table,
                            "domain": {
                                "name": physical_data_dictionary,
                                "community": {
                                    "name": "Schemas"
                                }
                            }
                        }
                    ]
                }
            }
            for column in columns
        ]
    ]

    logger.info(dictionary)
    json_str = json.dumps(dictionary)
    json_file = io.StringIO(json_str)

    return json_file, sync_id_value
