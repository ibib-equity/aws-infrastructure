
import json
import unittest

from collibra_api_integration import extract_api_info, generate_collibra_json
from tests.expected_payload import openapi_template, weather_api, trans_dist, asset_work_mgmt

class TestJsonProcessing(unittest.TestCase):

    def test_process_openapi_template_json_file(self):
        json_initial_payload_path = 'tests/json_payloads/openapi-template.json'
        with open(json_initial_payload_path, 'r') as f:
            initial_payload = json.loads(f.read())
        
        api_info, title = extract_api_info(initial_payload)
        assert title == "Swagger Petstore - OpenAPI 3.0"
        openapi_dictionary = generate_collibra_json(api_info)
        assert openapi_dictionary == openapi_template.expected_payload

    def test_process_enterprise_weather_json_file(self):
        json_initial_payload_path = 'tests/json_payloads/enterprise-weather-api.json'
        with open(json_initial_payload_path, 'r') as f:
            initial_payload = json.loads(f.read())
        
        api_info, title = extract_api_info(initial_payload)
        assert title == 'enterprise-weather-data-product-api-sbx'
        openapi_dictionary = generate_collibra_json(api_info)
        assert openapi_dictionary == weather_api.expected_payload

    def test_transmission_distribution_json_file(self):
        json_initial_payload_path = 'tests/json_payloads/transmission_and_distribution_api_spec.json'
        with open(json_initial_payload_path, 'r') as f:
            initial_payload = json.loads(f.read())
        
        api_info, title = extract_api_info(initial_payload)
        assert title == 'common-prod-api-gateway'
        openapi_dictionary = generate_collibra_json(api_info)
        assert openapi_dictionary == trans_dist.expected_payload

    def test_asset_work_management_json_file(self):
        json_initial_payload_path = 'tests/json_payloads/asset-work-management-api.json'
        with open(json_initial_payload_path, 'r') as f:
            initial_payload = json.loads(f.read())
        
        api_info, title = extract_api_info(initial_payload)
        assert title == 'Asset and Work Management API'
        openapi_dictionary = generate_collibra_json(api_info)
        assert openapi_dictionary == asset_work_mgmt.expected_payload
