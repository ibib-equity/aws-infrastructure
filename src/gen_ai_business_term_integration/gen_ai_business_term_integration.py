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
    the different functions to use gen ai to define business term.
    """
    microsoft_credentials = {
        "client_id": os.environ["azure_client_id"],
        "client_secret": os.environ["azure_client_secret"],
    }

    genie_credentials = {
        "client_id": os.environ["genie_client_id"],
        "client_secret": os.environ["genie_client_secret"],
    }

    microsoft_auth_url = os.environ["microsoft_auth_url"]
    auth_token = get_auth_token(microsoft_auth_url, microsoft_credentials)
    genie_scope = os.environ["genie_scope"]
    genie_url = os.environ["genie_url"]
    genie_auth_url = os.environ["genie_auth_url"]
    genie_auth_token = get_auth_token(genie_auth_url, genie_credentials, genie_scope)

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

    workflow_task_ids = find_gen_ai_define_workflow_instance(auth_token, collibra_api_endpoints)
    for workflow_task_id in workflow_task_ids:
        business_term = find_gen_ai_define_task(auth_token, workflow_task_id, collibra_api_endpoints)
        genie_definition = genie_define(genie_auth_token, genie_url, business_term)
        print(genie_definition)
        complete_task_instance(auth_token, workflow_task_id, collibra_api_endpoints, genie_definition)

def find_gen_ai_define_workflow_instance(auth_token, collibra_api_endpoints):
    """
    This function is used to find instances of the Gen AI Define workflow.
    We then grab the task uuid so we can grab the business term
    variable.
    """
    headers = {
    'Authorization': auth_token
    }

    payload = {
        'workflowDefinitionName': "Gen AI Define"
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


def find_gen_ai_define_task(auth_token, workflow_task_id, collibra_api_endpoints):
    """
    This function is used to find the task of the Gen AI Define workflow.
    We are grabbing business term variable to pass to genie to define.
    """
    headers = {
    'Authorization': auth_token
    }

    url = collibra_api_endpoints["workflow_task"] + str(workflow_task_id) + "/taskFormData"

    results = requests.get(url, headers=headers)

    business_term = results.json()["formProperties"][0]["value"]
    logger.info("business_term: " + str(business_term))
    
    return business_term

def genie_define(genie_auth_token, genie_url, business_term):
    """
    This function is used to get a definion from genie.
    """
    payload = {
        "conversationId": "f9b03105-fc9e-4d48-bacd-6fd549782d39",
        "employeeInfo": {
            "id": "468477",
            "name": "Finegan, Jack",
            "email": "Jack.Finegan@duke-energy.com",
            "department": "47453",
            "jobTitle": "Data Engineer"
        },
        "userInput": {
            "input": {
                "content": f"please define the business term, {business_term}, as it pertains to Duke Energy. Please keep your response to one to two sentences and only provide the definition.",
                "type": "text",
                "timestamp": 1738613010118,
                "createdBy": "user",
                "usecase": "Chat with LLM",
                "interactionId": "f9b03105-fc9e-4d48-bacd-6fd549782d38_1738613010118",
                "detailedAnalysis": f"false",
                "datasources": {
                    "selectAll": "true",
                    "selectedSources": [
                        {
                            "source": "Enterprise FAQs",
                            "key": "edcfaa97-b7eb-426f-a46e-02ae24a99be4"
                        },
                        {
                            "source": "DEX",
                            "key": "82f90e27-d5d3-4b9b-a71e-791269fcf98b"
                        },
                        {
                            "source": "About AI",
                            "key": "3e91afc2-caf8-48d0-9464-081f02f9a4e8"
                        },
                        {
                            "source": "Data Marketplace",
                            "key": "84c56833-6bcf-433b-b27b-7a747374c15b"
                        },
                        {
                            "source": "Data Marketplace POC",
                            "key": "7da710ab-45e3-4a47-823b-fc5529ad2613"
                        },
                        {
                            "source": "DE Cloud",
                            "key": "79119127-3962-44fb-abe7-392fc3b48c1a"
                        },
                        {
                            "source": "Enterprise Policies",
                            "key": "153fb2f9-518d-435b-bc66-0e8f97b20e29"
                        },
                        {
                            "source": "ACLtest",
                            "key": "d228398f-7979-45c2-bc94-ea1e86e0bf56"
                        },
                        {
                            "source": "IT 503 Program Docs",
                            "key": "65ba8a55-85aa-4ea7-ba3c-8b6ca1274d02"
                        },
                        {
                            "source": "Land Services",
                            "key": "a79dd125-d202-4c79-9fef-e915762aebfc"
                        },
                        {
                            "source": "Fruits",
                            "key": "c68e13a5-753e-4222-bae5-24f37d5938cb"
                        },
                        {
                            "source": "Telecom",
                            "key": "edb43428-21d9-4f87-80b3-4828ec8ef104"
                        },
                        {
                            "source": "Test",
                            "key": "c9996cfb-ecee-4557-a810-c42d5d71e066"
                        }
                    ]
                },
                "sources": []
            },
            "chatHistory": []
        },
        "metadata": {}
    }
    
    headers = {
        'Authorization': genie_auth_token
    }
    response = requests.post(genie_url, json=payload, headers=headers)
    response_json = response.json()
    genie_definition = response_json["messages"][0]["content"]
    return genie_definition

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

def complete_task_instance(auth_token, workflow_task_id, collibra_api_endpoints, genie_definition):
    """
    This function is used to complete the task and continue the flow.
    """
    payload = {
    "taskIds": [
        str(workflow_task_id)
        ],
    "taskFormProperties": {
        "genieDefinition": genie_definition
        }
    }
    url =  collibra_api_endpoints["workflow_task"] + 'completed'
    headers = {
        'Authorization': auth_token
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response)