import io
import json
import os
import uuid
import boto3
import datetime
import zipfile

from shared import requests, logging, get_auth_token

logger = logging.getLogger()
logger.setLevel("INFO")

s3_client = boto3.client('s3')

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
        "workflow_task": os.environ['collibra_url'] + "/workflowTasks/",
        "insights_reporting": os.environ['collibra_url'] + "/reporting/insights/directDownload?snapshotDate="
    }

    # Get date string to be used for insights api call and naming convention in s3
    date_str = (
        datetime.date.today() - datetime.timedelta(days=1)
        ).strftime("%Y-%m-%d")
    
    # Contruct download URL
    url = collibra_api_endpoints["insights_reporting"] + str(date_str) + "&format=zip"

    # Define local paths for file download and extraction
    local_zip_path = "/tmp/temp_file.zip"
    extract_dir = "/tmp/extracted"
    os.makedirs(extract_dir, exist_ok=True)

    # S3 bucket info
    bucket_name = os.environ["insights_reporting_bucket"]
    s3_prefix = f"insights/{date_str}"
    
    # Download insights zip
    download_zip(auth_token, url, local_zip_path)

    # Unzip files
    unzip_files(local_zip_path, extract_dir)

    # Upload files to s3 "insights/YYYY-MM-DD"
    files = upload_files_to_s3(extract_dir, bucket_name, s3_prefix)

    logger.info(
            f"Downloaded zip, extracted {files} files, and uploaded to s3://{bucket_name}/{s3_prefix}"
        )

def download_zip(auth_token, url, local_zip_path):
    """
    This function is used to download the zip file for 
    the insights reporting
    """
    
    headers = {
    'Authorization': auth_token
    }

    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(local_zip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def unzip_files(zip_path, extract_dir):
    """
    This function extracts the files from the zip file
    """

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_dir)

def upload_files_to_s3(local_dir, bucket_name, prefix):
    """
    This function loops through local_dir, and uploads each file to s3.

    Returns the number of files uploaded.
    """

    file_count = 0
    for root, dirs, files in os.walk(local_dir):
        for filename in files:
            file_count += 1
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_dir)

            s3_key = f"{prefix}/{relative_path}"

            s3_client.upload_file(
                Filename=local_path,
                Bucket=bucket_name,
                Key=s3_key
            )
    return file_count