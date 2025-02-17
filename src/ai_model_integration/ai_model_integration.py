import json
import requests
import logging
import os

from shared import get_auth_token, import_sync

logger = logging.getLogger()
logger.setLevel("INFO")

AZURE_CLIENT_ID = os.environ["azure_client_id"]
AZURE_CLIENT_SECRET = os.environ["azure_client_secret"]
MSFT_AUTH_URL = os.environ["microsoft_auth_url"]
COLLIBRA_API_URL = os.environ["collibra_url"]
DOMAIN_UUID = os.environ["model_domain_uuid"]
MODEL_ASSET_TYPE = os.environ["model_asset_type"]
DESCRIPTION = os.environ["model_description"]
VERSION = os.environ["model_version"]
INFERENCE_ENVIRONMENT = os.environ["model_inference_environment"]
TRAINING_ENVIRONMENT = os.environ["model_training_environment"]
PROBLEM_TYPE = os.environ["model_problem_type"]
ALGORITHM_TYPE = os.environ["model_algorithm_type"]
CREATOR = os.environ["model_creator"]
OWNER = os.environ["model_owner"]
BUSINESS_PROBLEM = os.environ["business_problem"]
BUSINESS_STAKEHOLDERS = os.environ["business_stakeholders"]
LINE_OF_BUSINESS = os.environ["line_of_business"]
INTENDED_USES_OF_THE_MODEL = os.environ["intended_uses_of_the_model"]
FACTORS_AFFECTING_MODEL_EFFICACY = os.environ["factors_affecting_model_efficacy"]
RISK_RATING = os.environ["risk_rating"]
EXPLANATIONS_FOR_RISK_RATING = os.environ["explanations_for_risk_rating"]


class CollibraAIGov:
    def __init__(self):
        # Unique identifier for the domain where all AI Model assets are stored
        self.domain = DOMAIN_UUID
        # Base URL for the Collibra API
        self.COLLIBRA_API_URL = COLLIBRA_API_URL

        self.MSFT_CREDS = {
            "client_id": AZURE_CLIENT_ID,
            "client_secret": AZURE_CLIENT_SECRET
        }

        self.MSFT_AUTH_URL = MSFT_AUTH_URL

        self.auth_token = get_auth_token(self.MSFT_AUTH_URL, self.MSFT_CREDS)

    def model_update_creation(
            self,
            model_details
    ):
        """
        Create a model and add all relevant information in the AI Governance Module.

        Parameters:
        - model_name: Name of the model to be created.
        - model_precision: Precision metric of the model (optional).
        - model_accuracy: Accuracy metric of the model (optional).
        - model_type: Type of the model (optional). Allowed values are "Generative AI", "Classification", "Regression",
        "Computer Vision", "Reinforcement Learning" or "Image Classification"
        """

        def builder(model_blob):
            """
            Constructs the query payload for model creation.

            Parameters:
            - model_name: Name of the model to be created.

            Returns:
            - A dictionary representing the query payload.
            """
            query = {
                "attributes": {
                    DESCRIPTION: [{"value": model_blob["model_description"]}],
                    VERSION: [{"value": model_blob["model_version"]}],
                    INFERENCE_ENVIRONMENT: [{"value": model_blob["inference_environment"]}],
                    TRAINING_ENVIRONMENT: [{"value": model_blob["training_environment"]}],
                    PROBLEM_TYPE: [{"value": model_blob["problem_type"]}],
                    ALGORITHM_TYPE: [{"value": model_blob["algorithm_type"]}],
                    CREATOR: [{"value": model_blob["model_creator"]}],
                    OWNER: [{"value": model_blob["model_owner"]}],
                    BUSINESS_PROBLEM: [{"value": model_blob["business_problem"]}],
                    # BUSINESS_STAKEHOLDERS: [{"value": model_blob["business_stakeholders"]}],
                    # LINE_OF_BUSINESS: [{"value": model_blob["line_of_business"]}],
                    INTENDED_USES_OF_THE_MODEL: [{"value": model_blob["intended_uses"]}],
                    FACTORS_AFFECTING_MODEL_EFFICACY: [{"value": model_blob["factors_affecting_model_efficiency"]}],
                    RISK_RATING: [{"value": model_blob["risk_rating"]}],
                    EXPLANATIONS_FOR_RISK_RATING: [{"value": model_blob["explanations_for_risk_rating"]}],
                },
                "displayName": model_blob["model_name"],
                "identifier": {
                    "domain": {
                        "name": "AI Models",
                        "community": {
                            "name": "AI Central Community",
                        },
                    },
                    "name": model_blob["model_name"],
                },
                "resourceType": "Asset",
                "type": {
                    "id": MODEL_ASSET_TYPE,
                },
            }
            logger.info(f"query: {query}")
            return query

        # Serialize the query payload to JSON
        query_payload = json.dumps([builder(model_details)])
        headers = {
            'accept': 'application/json',
            'Authorization': self.auth_token
        }
        # Construct the file object to be sent in the request
        file = {"file": ("data.json", query_payload)}

        # Make a POST request to the Collibra import API
        # Increase the timeout if the request takes longer
        response = requests.post(
            f"{self.COLLIBRA_API_URL}/import/json-job",
            files=file,
            headers=headers,
            timeout=30
        )

        # logger.info the response for debugging purposes
        # Consider handling the response more gracefully in a real application
        logger.info(response)


def lambda_handler(event, _):
    """
    This function handles the calling of the lambda. It expects to receive an event that contains the attributes of an
    AI model from AI Central.
    """

    logger.info(event)
    collibra = CollibraAIGov()
    collibra.model_update_creation(event["detail"])