

import boto3
import json
import os
import logging


logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, _):
    """
    This function takes the event from eventbridge, checks the source, and passes it to the appropriate lambda
    """
    logger.info(f"Event: {event}")
    event_source = check_event_source(event)
    logger.info(f"Event Source: {event_source}")
    response = invoke_lambda(event_source, event)
    logger.info(f"Response: {response}")
    outcome = response['Payload'].read()
    return outcome


def check_event_source(event):
    """
    This function is used to check the event that is coming through eventbridge. It then is used in invoke_lambda
    in order to invoke the correct lambda function.
    """
    event_source = event['source']
    return event_source


def invoke_lambda(event_source, event):
    """
    This function invokes the applicable lambda function based off of the event_source.
    """
    ai_model_integration = os.environ["ai_model_integration_lambda_arn"]
    api_spec_getter = os.environ["api_spec_getter_lambda_arn"]
    lambda_client = boto3.client('lambda')

    if event_source == 'new_model_lambda':
        response = lambda_client.invoke(
            FunctionName=ai_model_integration,
            InvocationType='Event',
            Payload=json.dumps(event)
        )

    if event_source == 'core_team_event':
        response = lambda_client.invoke(
            FunctionName=api_spec_getter,
            InvocationType='Event',
            Payload=json.dumps(event)
        )

    return response
