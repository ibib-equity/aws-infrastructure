"""
This is the shared auth class. Any function that is used more than
once should be placed here, eventually wrapped into a class.
"""
import requests
import logging

logger = logging.getLogger()

def get_auth_token(microsoft_auth_url, microsoft_credentials, scope=None):
    """
    This is for pulling the auth token from Azure.
    """
    body = {
        "grant_type": "client_credentials"
    }
    if scope:
        body["scope"] = scope
    r = requests.post(
        microsoft_auth_url,
        auth=(microsoft_credentials["client_id"], microsoft_credentials["client_secret"]),
        data=body,
    )
    auth_token = "Bearer " + r.json()["access_token"]
    return auth_token

def import_sync(collibra_api_endpoints, json_file, sync_id_value, auth_token):
    """
    This function is used in order to create assets (db,table,column,etc.) in collibra 
    in use cases where the changes must be tracked. The json_file is a .json file 
    which is what the import api from collibra expects. 
    
    """
    headers = {
        'accept': 'application/json',
        'Authorization': auth_token
    }
    files = {
        'finalizationStrategy': 'CHANGE_STATUS',
        'missingAssetStatusId': '52a0638e-121e-4633-b201-eb2d54ccb0b6',
        'continueOnError': 'false',
        'sendNotification': 'true',
        'deleteFile': 'false',
        'simulation': 'false',
        'fileName': 'sync-file',
        'file': json_file,
    }
    response = requests.post(collibra_api_endpoints["import_sync"] + str(sync_id_value) + '/json-job', headers=headers,
                             files=files)

    return response

