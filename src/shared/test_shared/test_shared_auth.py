"""
This is for testing any functions in the shared auth file
"""
import json
import os
from unittest import TestCase
from unittest.mock import patch

from shared import get_auth_token, import_sync

class TestSharedAuth(TestCase):
    """
    This is the class for testing shared auth.
    """
    @patch('requests.post')
    def test_shared_auth_post(self, mock_post):
        microsoft_auth_url = "www.testurl.com"
        microsoft_credentials = {"client_id": "value1", "client_secret": "value2"}
        get_auth_token(microsoft_auth_url, microsoft_credentials)
        mock_post.assert_called_with(microsoft_auth_url, data={"grant_type": "client_credentials"}, auth=("value1",
                                                                                                          "value2"))

class TestSharedImportPost(TestCase):
    """
    This is the class for testing shared import api.
    """
    @patch('requests.post')
    def test_shared_import_post(self, mock_post):
        collibra_api_endpoints = {'import_sync': 'www.testurl.com' + '/import/synchronize/'}
        auth_token = 1234
        json_file = "file.json"
        sync_id_value = "value_1"
        import_sync(collibra_api_endpoints, json_file, sync_id_value, auth_token)
        mock_post.assert_called_with("www.testurl.com/import/synchronize/value_1/json-job", headers={'accept': 'application/json', 'Authorization': 1234},
                                     files={'finalizationStrategy': 'CHANGE_STATUS', 'missingAssetStatusId': '52a0638e-121e-4633-b201-eb2d54ccb0b6', 'continueOnError': 'false', 
                                            'sendNotification': 'true', 'deleteFile': 'false', 'simulation': 'false', 'fileName': 'sync-file', 'file': 'file.json'})
        
