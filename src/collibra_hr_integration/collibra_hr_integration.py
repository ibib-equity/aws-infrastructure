"""
This function takes the hr details and adds them to collibra
"""
import os

from shared import logging, requests, get_auth_token

logger = logging.getLogger()


def lambda_handler(event, _):
    """
    This is where the details are passed into the lambda
    and parsed to be sent off to collibra
    """
    logger.info("Function called")

    microsoft_credentials = {
        "client_id": os.environ["azure_client_id"],
        "client_secret": os.environ["azure_client_secret"],
    }

    microsoft_auth_url = os.environ["microsoft_auth_url"]

    auth_token = get_auth_token(microsoft_auth_url, microsoft_credentials)

    headers = {
        'Authorization': auth_token
    }

    for item in event:
        src_network_id = item["payload"]["value"]["Source_Network_Id"]
        is_active = item["payload"]["value"]["Active_Indicator"]
        logger.info("Source_Network_Id  = " + str(src_network_id))
        logger.info("Is active = " + str(is_active))
        if is_active == "Y":
            pref_first_name = item["payload"]["value"]["Preferred_First_Name"]
            pref_last_name = item["payload"]["value"]["Preferred_Last_Name"]
            ext_email = item["payload"]["value"]["External_Email_Address"]

            payload = {
                "name": src_network_id,
                "displayName": src_network_id,
                "domainId": os.environ['domainId'],
                "typeId": os.environ['domainTypeId']
            }

            url = os.environ['collibra_url'] + "/assets"

            response = requests.post(url, headers=headers, json=payload)

            logger.info("Response from creating asset = " + str(response.json()))

            if response.status_code == 201:
                asset_id = response.json()["id"]

                payload_fname_attr = {
                    "assetId": asset_id,
                    "typeId": os.environ['firstnameAttrTypeId'],
                    "value": pref_first_name
                }

                url_attr = os.environ['collibra_url'] + "/attributes"
                response_fname_attr = requests.post(url_attr, headers=headers, json=payload_fname_attr)
                logger.info("Response from updating FName Attr = " + str(response_fname_attr.status_code))

                payload_lname_attr = {
                    "assetId": asset_id,
                    "typeId": os.environ['lastnameAttrTypeId'],
                    "value": pref_last_name,
                }

                response_lname_attr = requests.post(url_attr, headers=headers, json=payload_lname_attr)
                logger.info("Response from updating last name attribute = " + str(response_lname_attr.status_code))

                payload_email_attr = {
                    "assetId": asset_id,
                    "typeId": os.environ['emailAttrTypeId'],
                    "value": ext_email,
                }

                response_email_attr = requests.post(url_attr, headers=headers, json=payload_email_attr)
                logger.info("Response from updating email attribute = " + str(response_email_attr.status_code))
                logger.info("Asset created and attributes updated successfully")

    logger.info("out of loop")
