"""
This lambda receives an event from two kafka sink connectors. One runs against the Corporate Kafka Schema Registry
and the other against the Nuclear Kafka Schema Registry. Both send over table and column names along with data types.
The events are checked to verify they are the schema changes we are looking for, the schema is formatted as JSON, and
then formatted into an object consumable by Collibra. The schema is also flattened.

Once the formatting finishes, the object is sent to Collibra under either Kafka or Nuclear Kafka
"""

import json
import logging
import os
import io
import requests

from shared import get_auth_token, import_sync

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, _):
    """
    This is where we will parse the event and call functions against it
    """
    logger.info(event)

    results = []
    for ind_event in event:
        try:
            request_key, request_value = parse_event(ind_event['payload'])
            valid_event = validate_event(request_key, request_value)
            logger.info(
                f"This event has been judged valid, and will be ran through the rigamarole...")
            logger.info(f"JSON Value: {valid_event}")
            flattened_fields = flatten_fields(valid_event["schema"]["fields"])
            fields_extract, table_name, table_version = prep_payload(valid_event, flattened_fields)
            query_payload = builder(fields_extract, table_name, table_version)
            files, headers = construct_request(query_payload)
            results.append(submit_request(files, headers))

        except Exception as e:
            logger.info(f"Error processing {ind_event}: {e}")
            continue

    return results


def parse_event(ind_event):
    """
    Take a validated individual event and formats it as json.

    takes: valid_event, a string that looks like a dictionary

    returns: parsed event, an actual dictionary formatted as json
    """
    logger.info(f"Payload event: {ind_event}")
    request_key = json.loads(ind_event['key'])
    if ind_event['value'] is not None:
        request_value = json.loads(ind_event['value'].replace('\\', '').replace('"{', '{').replace('}"', '}'))
    else:
        raise Exception("This payload contains no Value")
    logger.info(f"Request Key: {request_key}")
    logger.info(f"Request Value: {request_value}")

    return request_key, request_value


def validate_event(request_key, request_value):
    """

    """
    if request_key["keytype"] == "SCHEMA":
        if "-key" in request_value["subject"]:
            raise Exception("This payload is a -key type, moving on to the next")
        if "fields" not in request_value["schema"]:
            raise Exception(f"Fields and columns not located in the payload {request_value}")
    else:
        raise Exception("This payload is not a SCHEMA type, moving on to the next")

    return request_value


def submit_request(ind_headers, ind_files):
    # Make a POST request to the Collibra import API
    # Increase the timeout if the request takes longer
    collibra_url = os.environ["collibra_url"]
    response = requests.post(
        f"{collibra_url}/import/json-job",
        files=ind_files,
        headers=ind_headers,
        timeout=30
    )

    # logger.info the response for debugging purposes
    # Consider handling the response more gracefully in a real application
    logger.info(response)
    return {'statusCode': 200, 'body': "Message successfully processed"}


def construct_request(ind_query):
    msft_creds = {
        "client_id": os.environ["azure_client_id"],
        "client_secret": os.environ["azure_client_secret"]
    }

    auth_token = get_auth_token(os.environ["microsoft_auth_url"], msft_creds)

    ind_headers = {
        'accept': 'application/json',
        'Authorization': auth_token
    }
    # Construct the file object to be sent in the request
    json_str = json.dumps(ind_query)
    json_file = io.StringIO(json_str)
    ind_files = {
        'continueOnError': 'false',
        'sendNotification': 'false',
        'deleteFile': 'false',
        'simulation': 'false',
        'fileName': 'sync-file',
        'relationsAction': 'REPLACE',
        'file': json_file
    }

    logger.info(ind_files)
    return ind_headers, ind_files


def _flatten_dict_gen(nested_dict):
    for field in nested_dict:
        if isinstance(field["type"], dict) and "fields" in field["type"]:
            yield from flatten_dict(field["type"]["fields"])
        else:
            yield field


def flatten_dict(nested_dict):
    return _flatten_dict_gen(nested_dict)


def flatten_fields(fields):
    new_fields = []
    for field in fields:
        if isinstance(field["type"], dict) and "fields" in field["type"]:
            temp_dict = flatten_dict(field["type"]["fields"])
            for entry in temp_dict:
                new_fields.append(entry)
            field["type"] = "record"
            if "default" not in field:
                field["default"] = "None"
            new_fields.append(field)
        else:
            new_fields.append(field)
    return new_fields


def prep_payload(table_details, fields):
    try:
        name = table_details["subject"].removesuffix("-value")
    except ValueError:
        name = table_details["subject"]

    logger.info(f"We have extracted these fields...\n{fields}")

    try:
        for field in fields:
            if isinstance(field["type"], str):
                pass
            elif isinstance(field["type"], list):
                field["type"].remove("null")
                if isinstance(field["type"][0], dict):
                    field["type"] = field["type"][0]["type"]
                else:
                    field["type"] = next(iter((field["type"])))
            if isinstance(field["type"], dict):
                field["type"] = field["type"]["type"]
            logger.info("The type of this field is...")
            logger.info(type(field["type"]))
    except ValueError:
        pass  # do nothing!

    version = table_details["version"]

    return fields, name, version


def builder(fields, name, version):
    domain_name = os.environ["kafka_sink_domain_uuid"]
    query = [
        {
            "displayName": domain_name,
            "identifier": {
                "domain": {
                    "name": domain_name,
                    "community": {
                        "name": "Schemas",
                    },
                },
                "name": domain_name,
            },
            "resourceType": "Asset",
            "type": {
                "name": "Schema",
            }
        },
        {
            "resourceType": "Asset",
            "identifier": {
                "name": name,
                "domain": {
                    "name": domain_name,
                    "community": {
                        "name": "Schemas"
                    }
                }
            },
            "type": {
                "name": "Table"
            },
            "relations": {
                "00000000-0000-0000-0000-000000007043:SOURCE": [
                    {
                        "name": domain_name,
                        "domain": {
                            "name": domain_name,
                            "community": {
                                "name": "Schemas"
                            }
                        }
                    }
                ]
            },
            "attributes": {
                "Version": [
                    {
                        "value": version
                    }
                ]
            }
        },
        [
            {
                "resourceType": "Asset",
                "identifier": {
                    "name": item["name"],
                    "domain": {
                        "name": domain_name,
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
                            "value": item["type"]
                        }
                    ]
                },
                "relations": {
                    "00000000-0000-0000-0000-000000007042:TARGET": [
                        {
                            "name": name,
                            "domain": {
                                "name": domain_name,
                                "community": {
                                    "name": "Schemas"
                                }
                            }
                        }
                    ]
                }
            }
            for item in fields
        ]
    ]
    logger.info(f"query: {query}")
    return query
