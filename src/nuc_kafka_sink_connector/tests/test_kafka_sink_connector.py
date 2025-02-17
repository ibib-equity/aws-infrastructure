import os
import unittest
from unittest.mock import patch
from tests.expected_payload.invalid_kafka_sink_connector_payload import non_schema_payload, key_payload
from tests.expected_payload.valid_kafka_sink_connector_payload import valid_single_payload, valid_multipart_payload, \
    valid_nestedfields_payload
from nuc_kafka_sink_connector import lambda_handler


class TestKafkaSinkConnector(unittest.TestCase):
    @patch.dict(os.environ, values={
        'azure_client_id': 'foo',
        'azure_client_secret': 'ofo',
        'microsoft_auth_url': 'oof',
        'collibra_url': 'foo',
        'kafka_sink_col_names_uuid': 'ofo',
        'kafka_sink_table_asset_uuid': 'oof',
        'nuclear_topic_name': 'foo',
        'corp_topic_name': 'ofo',
        'nuclear_domain_name': 'oof',
        'corp_domain_name': 'foo',
        'kafka_sink_domain_uuid': 'ofo'
    })
    def test_valid_kafka_sink_connector_payload(self):
        response = lambda_handler(valid_single_payload, None)
        print(response)
        self.assertEqual(200, response["statusCode"])

    def test_valid_multipart_kafka_sink_connector_payload(self):
        response = lambda_handler(valid_multipart_payload, None)
        print(response)
        self.assertEqual(200, response["statusCode"])

    def test_valid_nested_fields_kafka_sink_connector_payload(self):
        response = lambda_handler(valid_nestedfields_payload, None)
        print(response)
        self.assertEqual(200, response["statusCode"])

    def test_keypayload_kafka_connector_sink_payload(self):
        with self.assertRaises(Exception):
            lambda_handler(key_payload, None)

    def test_nonschema_kafka_connector_sink_payload(self):
        response = lambda_handler(non_schema_payload, None)
        print(response)
        self.assertEqual(400, response["statusCode"])

    def test_missing_kafka_connector_sink_payload(self):
        response = lambda_handler("", None)
        print(response)
        self.assertEqual(400, response["statusCode"])


if __name__ == '__main__':
    unittest.main()
