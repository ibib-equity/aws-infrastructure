"""
This lambda function will be triggered by a file being uploaded to s3.
We will take in the event, pull the content of the file, parse the json,
push the openapi spec into collibra, then move file to processed folder
in s3.
"""

import io
import json
import os
import uuid
import boto3
import logging

from shared import get_auth_token, import_sync

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, _):
    """
    The lambda handler is the intake for this lambda function.
    This will receive the event object, and pass the data between
    the different functions until it is written to the dynamodb.
    """
    microsoft_credentials = {
        "client_id": os.environ["azure_client_id"],
        "client_secret": os.environ["azure_client_secret"],
    }

    microsoft_auth_url = os.environ["microsoft_auth_url"]
    auth_token = get_auth_token(microsoft_auth_url, microsoft_credentials)

    collibra_api_endpoints = {
        "assets": os.environ['collibra_url'] + "/assets",
        "assets_bulk": os.environ['collibra_url'] + "/assets/bulk",
        "relations_bulk": os.environ['collibra_url'] + "/relations/bulk",
        "relations": os.environ['collibra_url'] + "/relations",
        "domains": os.environ['collibra_url'] + "/domains",
        "attributes": os.environ['collibra_url'] + "/attributes",
        "import_sync": os.environ['collibra_url'] + "/import/synchronize/",
        "workflow_start": os.environ['collibra_url'] + "/workflowInstances",
        "workflow_definition": os.environ['collibra_url'] + "/workflowDefinitions"
    }

    openapi_payload, bucket_name, source_key = grab_file_content_from_s3(event)
    api_info, title = extract_api_info(openapi_payload)
    sync_id_value = sync_id_find(title)
    openapi_dictionary = generate_collibra_json(api_info)
    logger.info(openapi_dictionary)
    json_str = json.dumps(openapi_dictionary)
    json_file = io.StringIO(json_str)
    sync_result = import_sync(collibra_api_endpoints, json_file, sync_id_value, auth_token)
    logger.info(sync_result)
    move_file_to_processed_folder(bucket_name, source_key)


def sync_id_find(title):
    """
    The sync_id_find function expects the title variable which
    it uses to read the sync id from dynamodb if it exists, if it
    does not exist it will create a new sync id
    """
    logger.info("Checking DynamoDB for the sync id.")
    dynamodb = boto3.client('dynamodb')
    dynamodb_table = os.environ["dynamodb_table"]
    api_title_name = title
    try:
        response = dynamodb.get_item(
            TableName=dynamodb_table,
            Key={
                'api-title-name': {'S': api_title_name}
            }
        )
        if 'Item' in response:
            item = response['Item']
            api_value = item.get('api-title-name', {}).get('S', '')
            sync_id_value = item.get('sync-id', {}).get('S', '')
            logger.debug(f'api_value Value: {api_value}, sync_id_value Value: {sync_id_value}')
            return sync_id_value
        else:
            logger.info('item not found in dynamodb, creating new record')
            random_uuid = uuid.uuid4()
            sync_id_value = str(random_uuid)
            item_to_add = {
                'api-title-name': {'S': api_title_name},
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


def grab_file_content_from_s3(event):
    """
    This function gets the file content from s3 based on
    the event.
    """
    logger.info("Grabbing the file from S3 using the following event...")
    logger.info(event)
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    s3 = boto3.client('s3')
    try:
        file_obj = s3.get_object(Bucket=bucket_name, Key=source_key)
        file_content = file_obj['Body'].read().decode('utf-8')
        openapi_payload = json.loads(file_content)
        return openapi_payload, bucket_name, source_key
    except Exception as e:
        logger.info(f'Error reading file {source_key} from bucket {bucket_name}: {str(e)}')
        raise


def move_file_to_processed_folder(bucket_name, source_key):
    """
    This function moves the file from intake folder to processed folder
    """
    logger.info("Moving the processed S3 file to the processed-openapi-spec folder.")
    destination_key = f'processed-openapi-spec/{source_key.split("/")[-1]}'
    s3 = boto3.client('s3')
    try:
        s3.copy_object(
            Bucket=bucket_name,
            CopySource={'Bucket': bucket_name, 'Key': source_key},
            Key=destination_key
        )

        s3.delete_object(
            Bucket=bucket_name,
            Key=source_key
        )
    except Exception as e:
        logger.info(f'Error moving file {source_key} to {destination_key}: {str(e)}')
        raise


def resolve_ref(openapi_payload, ref, resolved_refs=None):
    """
    This function is used to resolve $ref references in the openapi spec
    """
    if resolved_refs is None:
        resolved_refs = {}
    parts = ref.replace('#/', '').split('/')
    result = openapi_payload
    for part in parts:
        result = result[part]
    if '$ref' in result:
        ref_path = result['$ref']
        if ref_path in resolved_refs:
            return resolved_refs[ref_path]
        else:
            resolved_refs[ref_path] = resolve_ref(openapi_payload, ref_path, resolved_refs)
            return resolved_refs[ref_path]
    return result


def extract_properties(schema, openapi_payload, resolved_refs=None, parent_prefix=""):
    """
    This function is used to extract properties from the schema
    """
    if resolved_refs is None:
        resolved_refs = {}
    if schema is None:
        return {}
    if '$ref' in schema:
        schema_name = schema['$ref'].split('/')[-1]
        schema = resolve_ref(openapi_payload, schema['$ref'], resolved_refs)
        if schema_name == "empty" and 'properties' not in schema:
            logger.info(f"Skipping 'empty' schema with no properties for {schema_name}")
            return {}

    return handle_schema(schema, openapi_payload, resolved_refs, parent_prefix)


def handle_schema(schema, openapi_payload, resolved_refs, parent_prefix):
    properties = {}
    if 'properties' in schema:
        properties.update(handle_object(schema['properties'], openapi_payload, resolved_refs, parent_prefix))
    elif 'type' in schema and schema['type'] == 'array':
        properties.update(handle_array(schema, openapi_payload, resolved_refs, parent_prefix))
    else:
        properties[parent_prefix.rstrip(' > ')] = schema.get('type', 'unknown')
    return properties


def handle_object(properties, openapi_payload, resolved_refs, parent_prefix):
    result = {}
    for prop_name, prop_details in properties.items():
        full_name = f"{parent_prefix}{prop_name}" if parent_prefix else prop_name
        if '$ref' in prop_details or 'properties' in prop_details or ('type' in prop_details and prop_details['type'] == 'array'):
            nested_properties = extract_properties(prop_details, openapi_payload, resolved_refs, full_name + " > ")
            result.update(nested_properties)
        else:
            result[full_name] = prop_details.get('type', 'unknown')
    return result


def handle_array(schema, openapi_payload, resolved_refs, parent_prefix):
    properties = {}
    item_details = schema.get('items', {})
    if '$ref' in item_details:
        item_details = resolve_ref(openapi_payload, item_details['$ref'], resolved_refs)
    if 'properties' in item_details or '$ref' in item_details:
        properties.update(extract_properties(item_details, openapi_payload, resolved_refs, parent_prefix))
    else:
        properties[parent_prefix.rstrip(' > ')] = 'array'
    return properties
    

def extract_api_info(openapi_payload):
    api_info = {
        'api_name': openapi_payload['info']['title'],
        'description': openapi_payload['info'].get('description', 'No description provided'),
        'server_url': openapi_payload['servers'][0]['url'] if openapi_payload['servers'] else 'No server specified',
        'endpoints': []
    }
    logger.info("Extracting API Information...")
    title = api_info['api_name']
    for path, methods in openapi_payload['paths'].items():
        for method, details in methods.items():
            if method.upper() == 'OPTIONS':
                logger.info(f"Skipping OPTIONS for {path}")
                continue
            full_path = method.upper() + " " + path
            logger.info(f"Processing {full_path}...")
            if '200' in details['responses']:
                response_200 = details['responses']['200']
                if 'content' in response_200 and 'application/json' in response_200['content']:
                    schema_ref = response_200['content']['application/json'].get('schema', {})
                    if '$ref' in schema_ref:
                        table_name = schema_ref['$ref'].split('/')[-1]
                    elif 'items' in schema_ref and '$ref' in schema_ref['items']:
                        table_name = schema_ref['items']['$ref'].split('/')[-1]
                    else:
                        table_name = full_path + " Default Table"
                    
                    if 'type' in schema_ref and schema_ref['type'] in ['object', 'array', 'string'] and not schema_ref.get('properties'):
                        logger.info(f"Skipping detailed processing for {full_path} as the schema is simple.")
                        api_info['endpoints'].append({'path': full_path})
                        continue

                    columns = extract_properties(schema_ref, openapi_payload)
                    table = {'name': table_name, 'columns': [{'name': k, 'type': v} for k, v in columns.items()]}
                    api_info['endpoints'].append({'path': full_path,
                                                  'table': table})
                    logger.info(f"Added endpoint: {full_path}")
                else:
                    logger.info(f"No content or schema found for response 200 in {method.upper()} {path}")
            else:
                logger.info(f"No 200 response found for {full_path}")
    logger.info(api_info)
    return api_info, title


def generate_collibra_json(api_info):
    openapi_dictionary = []
    domain_name = api_info['api_name']
    community_name = "APIs"

    # Create our physical data dictionary where api will live
    physical_data_dictionary_domain = {
        "resourceType": "Domain",
        "identifier": {
            "name": api_info['api_name'],
            "community": {
                "name": community_name
            }
        },
        "type": {
            "name": "Physical Data Dictionary"
        }
    }
    openapi_dictionary.append(physical_data_dictionary_domain)

    # Create api asset
    api_asset = {
        "resourceType": "Asset",
        "identifier": {
            "name": api_info['api_name'],
            "domain": {
                "name": domain_name,
                "community": {
                    "name": community_name
                }
            }
        },
        "attributes": {
            "Description": [
                {
                    "value": api_info['description']
                }
            ],
            "URL": [
                {
                    "value": api_info['server_url']
                }
            ]
        },
        "type": {
            "name": "API"
        },
        "relations": {
            "00000000-0000-0000-0000-000000007005:SOURCE": [

            ]
        }
    }

    api_relations = []

    for endpoint in api_info['endpoints']:
        endpoint_name = endpoint['path']

        # Create api endpoint asset
        endpoint_asset = {
            "resourceType": "Asset",
            "identifier": {
                "name": endpoint_name,
                "domain": {
                    "name": domain_name,
                    "community": {
                        "name": community_name
                    }
                }
            },
            "type": {
                "name": "API Endpoint"
            },
            "relations": {
                "00000000-0000-0000-0000-000000007005:TARGET": [
                    {
                        "name": api_info['api_name'],
                        "domain": {
                            "name": domain_name,
                            "community": {
                                "name": community_name
                            }
                        }
                    }
                ]
            }
        }

        # Add relation from API to Endpoint
        api_relations.append(
            {
                "name": endpoint_name,
                "domain": {
                    "name": domain_name,
                    "community": {
                        "name": community_name
                    }
                }
            }
        )

        # add endpoint asset to dictionary
        openapi_dictionary.append(endpoint_asset)

        # Define table asset for the endpoint
        if 'table' in endpoint and 'name' in endpoint['table']:
            table_name = endpoint['table']['name']
            table_asset = {
                "resourceType": "Asset",
                "identifier": {
                    "name": table_name,
                    "domain": {
                        "name": domain_name,
                        "community": {
                            "name": community_name
                        }
                    }
                },
                "type": {
                    "name": "Table"
                },
                "relations": {
                    "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE": [
                        {
                            "name": endpoint_name,
                            "domain": {
                                "name": domain_name,
                                "community": {
                                    "name": community_name
                                }
                            }
                        }
                    ],
                    "00000000-0000-0000-0000-000000007042:SOURCE": [

                    ]
                }
            }

            # Add relation from Endpoint to Table
            endpoint_asset["relations"]["018da964-d53a-7b18-a8c8-044dbd47a622:TARGET"] = [
                {
                    "name": table_name,
                    "domain": {
                        "name": domain_name,
                        "community": {
                            "name": community_name
                        }
                    }
                }
            ]

            # process columns and their relations
            for column in endpoint['table']['columns']:
                column_name = column.get('name') if column.get('name', '').strip() else 'empty'
                column_type = column['type']
                column_asset = {
                    "resourceType": "Asset",
                    "displayName": column_name.split(' > ')[-1].strip(),
                    "identifier": {
                        "name": table_name + " > " + column_name,
                        "domain": {
                            "name": domain_name,
                            "community": {
                                "name": community_name
                            }
                        }
                    },
                    "type": {
                        "name": "Column"
                    },
                    "attributes": {
                        "Data Type": [
                            {
                                "value": column_type
                            }
                        ]
                    },
                    "relations": {
                        "00000000-0000-0000-0000-000000007042:TARGET": [
                            {
                                "name": table_name,
                                "domain": {
                                    "name": domain_name,
                                    "community": {
                                        "name": community_name
                                    }
                                }
                            }
                        ]
                    }
                }
                openapi_dictionary.append(column_asset)

                # add relation from Table to Column
                table_asset["relations"]["00000000-0000-0000-0000-000000007042:SOURCE"].append(
                    {
                        "name": table_name + " > " + column_name,
                        "domain": {
                            "name": domain_name,
                            "community": {
                                "name": community_name
                            }
                        }
                    }
                )

            # add table asset to dictionary
            openapi_dictionary.append(table_asset)

        else:
            logger.info(f"Not creating tables and columns for {endpoint['path']}")

    # add all endpoint relations to the API asset
    for relation in api_relations:
        api_asset["relations"]["00000000-0000-0000-0000-000000007005:SOURCE"].append(relation)

    openapi_dictionary.insert(1, api_asset)

    return openapi_dictionary
