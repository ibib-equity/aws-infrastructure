import os
import json
import unittest
from unittest.mock import patch
from tests.expected_payload.valid_kafka_sink_connector_payload import valid_single_payload, valid_multipart_payload, \
    valid_nestedfields_payload, correct_fields, parsed_fields, valid_request_payload
from nuc_kafka_sink_connector import validate_event, parse_event, flatten_fields, prep_payload, builder, construct_request


class TestIndividualKafkaSinkConnectorFunctions(unittest.TestCase):
    @patch.dict(os.environ, values={
        'azure_client_id': 'foo',
        'azure_client_secret': 'ofo',
        'microsoft_auth_url': 'oof',
        'collibra_url': 'foo',
        'kafka_sink_col_names_uuid': 'ofo',
        'kafka_sink_table_asset_uuid': 'oof',
        'collibra_topic_name': '_schemasdev1',
        'collibra_domain_name': 'oof',
        'kafka_sink_domain_uuid': 'ofo'
    })
    def test_parse_event(self):
        valid_request_key = json.loads(valid_single_payload[0]['payload']['key'])
        valid_request_value = json.loads(
            valid_single_payload[0]['payload']['value'].replace('\\', '').replace('"{', '{').replace('}"', '}'))
        request_key, request_value = parse_event(valid_single_payload[0]['payload'])
        self.assertEqual(valid_request_key, request_key)
        self.assertEqual(valid_request_value, request_value)

    def test_validate_event(self):
        valid_request_key = json.loads(valid_single_payload[0]['payload']['key'])
        valid_request_value = json.loads(
            valid_single_payload[0]['payload']['value'].replace('\\', '').replace('"{', '{').replace('}"', '}'))
        request_value = validate_event(valid_request_key, valid_request_value)
        self.assertEqual(valid_request_value, request_value)

    def test_flatten_fields(self):
        valid_request_value = json.loads(
            valid_nestedfields_payload[0]['payload']['value'].replace('\\', '').replace('"{', '{').replace('}"', '}'))
        fields = flatten_fields(valid_request_value["schema"]["fields"])
        self.assertEqual(correct_fields, fields)

    def test_prep_payload(self):
        valid_event = json.loads(
            valid_single_payload[0]['payload']['value'].replace('\\', '').replace('"{', '{').replace('}"', '}'))
        fields = valid_event["schema"]["fields"]
        fields_extract, table_name, table_version = prep_payload(
            valid_event, fields)
        self.assertEqual(parsed_fields, fields_extract)
        self.assertEqual(valid_event["subject"].removesuffix("-value"), table_name)
        self.assertEqual(valid_event["version"], table_version)

    @patch.dict(os.environ, values={
        'azure_client_id': 'foo',
        'azure_client_secret': 'ofo',
        'microsoft_auth_url': 'oof',
        'collibra_url': 'foo',
        'kafka_sink_col_names_uuid': 'ofo',
        'kafka_sink_table_asset_uuid': 'oof',
        'collibra_topic_name': '_schemasdev1',
        'collibra_domain_name': 'oof',
        'kafka_sink_domain_uuid': 'ofo'
    })
    def test_builder(self):
        valid_event = json.loads(
            valid_single_payload[0]['payload']['value'].replace('\\', '').replace('"{', '{').replace('}"', '}'))
        query_payload = builder(parsed_fields, valid_event["subject"].removesuffix("-value"), valid_event["version"])
        self.assertEqual(valid_request_payload, query_payload)


if __name__ == '__main__':
    unittest.main()
