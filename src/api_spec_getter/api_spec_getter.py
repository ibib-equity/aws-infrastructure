"""
This lambda function is triggered by the creation or modification of an API Gateway
It then contacts that API Gateway and retrieves the Open API spec from their endpoint.
"""

import json
import os
import boto3
import requests
import logging

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, _):
    """
    The lambda handler function pulls the endpoint url and stage name from the event.
    It then uses the endpoint url to extract the openapi in json format from the endpoint.
    :param event:
    :param _:
    :return:
    """

    stage_name, endpoint_url = extract_deployment_info(event)
    openapi_payload = get_json_from_endpoint(endpoint_url)
    return trigger_collibra_api_integration(openapi_payload)


def extract_deployment_info(event):
    """
    This function pulls the endpoint_url and stage_name from the event object and returns them.
    :param event:
    :return:
    """
    logger.info("Extracting the stage name and endpoint url from the event...")
    cloudtrail_event = event['requestParameters']
    stage_name = cloudtrail_event['stageName']
    endpoint_url = cloudtrail_event['description']
    logger.debug("stage_name: " + stage_name)
    logger.debug("endpoint_url: " + endpoint_url)

    return stage_name, endpoint_url


def get_json_from_endpoint(endpoint_url):
    """
    This function retrieves the openapi json object from the endpoint url.
    :param endpoint_url:
    :return:
    """
    logger.info("Retrieving the openapi json object from the API Gateway endpoint...")
    response = requests.get(endpoint_url)

    return response.json()


def trigger_collibra_api_integration(openapi_payload):
    """
    This function passes the openapi_payload to the collibra_api_integration lambda.
    :param openapi_payload:
    :return:
    """
    logger.info("Triggering the collibra api integration lambda with the openapi payload...")
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName=os.environ["collibra_api_integration_lambda_arn"],
        InvocationType='Event',
        Payload=json.dumps(openapi_payload)
    )

    return response
