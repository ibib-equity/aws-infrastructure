import io
import json
import os
import uuid
import boto3

from shared import requests, logging, get_auth_token

logger = logging.getLogger()
logger.setLevel("INFO")


def lambda_handler(event, _):
    """
    The lambda handler is the intake for this lambda function.
    This will receive the event object, and pass the data between
    the different functions to send teams message and email via 
    power automate flow.
    """
    microsoft_credentials = {
        "client_id": os.environ["azure_client_id"],
        "client_secret": os.environ["azure_client_secret"],
    }

    send_teams_message_invoke_url = os.environ["send_teams_message_invoke_url"]
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
        "workflow_definition": os.environ['collibra_url'] + "/workflowDefinitions",
        "workflow_instance": os.environ['collibra_url'] + "/workflowInstances",
        "workflow_task": os.environ['collibra_url'] + "/workflowTasks/"
    }

    workflow_task_ids = find_send_teams_message_workflow_instance(auth_token, collibra_api_endpoints)
    for workflow_task_id in workflow_task_ids:
        groupName, groupMessage, groupMembers = find_send_teams_message_task(auth_token, workflow_task_id, collibra_api_endpoints)
        invoke_send_teams_message_and_email_automate_flow(send_teams_message_invoke_url, groupName, groupMessage, groupMembers)
        cancel_task_instance(auth_token, workflow_task_id, collibra_api_endpoints)

def find_send_teams_message_workflow_instance(auth_token, collibra_api_endpoints):
    """
    This function is used to find instances of the Send Teams Message workflow.
    We then grab the task uuid so we can grab the groupName,groupMembers,groupMessage
    variables.
    """
    headers = {
    'Authorization': auth_token
    }

    payload = {
        'workflowDefinitionName': "Send Teams Message"
    }
    url = collibra_api_endpoints["workflow_instance"]

    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    results = data.get('results', [])
    logger.info(F"total number of instances: {len(results)}")

    workflow_task_ids = []

    for instance in results:
        instance_id = instance.get('id')
        tasks = instance.get('tasks', [])
        logger.info(f"Instance ID: {instance_id}, number of tasks: {len(tasks)}")
        for task in tasks:
            workflow_task_id = task.get('id')
            logger.info(f"Task ID: {workflow_task_id}")
            workflow_task_ids.append(workflow_task_id)
    
    return workflow_task_ids


def find_send_teams_message_task(auth_token, workflow_task_id, collibra_api_endpoints):
    """
    This function is used to find the task of the Send Teams Message workflow.
    We are grabbing groupName,groupMessage,groupMembers variables so we 
    can pass these into the send teams message/email power automate flow.
    """
    headers = {
    'Authorization': auth_token
    }

    url = collibra_api_endpoints["workflow_task"] + str(workflow_task_id) + "/taskFormData"

    results = requests.get(url, headers=headers)

    groupName = results.json()["formProperties"][0]["value"]
    logger.info("groupName: " + str(groupName))
    groupMessage = results.json()["formProperties"][1]["value"]
    groupMembers =results.json()["formProperties"][2]["value"]
    
    return groupName, groupMessage, groupMembers

def invoke_send_teams_message_and_email_automate_flow(send_teams_message_invoke_url, groupName, groupMessage, groupMembers):
    """
    This function is used to invoke the Power Automate Flow that will send 
    a message in Teams as well as email. It expects groupName, groupMessage, groupMembers variables.
    """
    payload = {
    "groupName": groupName,
    "groupMessage": groupMessage,
    "groupMembers": groupMembers
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(
        send_teams_message_invoke_url,
        json=payload,
        headers=headers
    )
    logger.info(r)

def cancel_task_instance(auth_token, workflow_task_id, collibra_api_endpoints):
    """
    This function is used to clear the send teams message task out of the queue
    in Collibra after the teams message and email have been sent.
    """
    url =  collibra_api_endpoints["workflow_task"] + str(workflow_task_id) + '/canceled'
    headers = {
        'Authorization': auth_token
    }
    response = requests.post(url, headers=headers)