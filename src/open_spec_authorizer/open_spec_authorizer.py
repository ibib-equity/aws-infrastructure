import json
import jwt
import requests
import os
import logging
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger()
logger.setLevel("INFO")

tenant_id = os.environ['TENANT_ID']
audience = os.environ['AUDIENCE']

def lambda_handler(event, context):
    logger.info(event)
    token_data = event['authorizationToken']
    if token_data is None:
        raise Exception("Token missing")
    token_type = 'JWT'

    jwt_token = token_data.split()[len(token_data.split()) - 1] if len(
        token_data.split()) > 1 else token_data
    
    logger.info(jwt_token)

    try:
        appid = decode_token(tenant_id, audience, jwt_token, token_type)['appid']
        logger.info(appid)
    except Exception as e:
        print(f"Token verification failed: {str(e)}")
        return generate_policy('user', 'deny', event['methodArn'])
    else:
        return generate_policy(appid, 'Allow', event['methodArn'])

    
def generate_policy(principal_id, effect, resource):
    """
    Generates an IAM policy document that allows or denies access to the API Gateway.
    """
    policy_document = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Action': 'execute-api:Invoke',
                'Effect': effect,
                'Resource': resource
            }
        ]
    }

    return {
        'principalId': principal_id,
        'policyDocument': policy_document
    }

def decode_token(tenant_id, audience, token, token_type):
    # By default, an access token is expected which will use sts.windows.net as issuer
    issuer = f'https://sts.windows.net/{tenant_id}/'
    if token_type == 'id':
        issuer = f'https://login.microsoftonline.com/{tenant_id}/v2.0'
    audience = f'{audience}'
    
    well_known_res = requests.get(f'https://login.microsoftonline.com/{tenant_id}/.well-known/openid-configuration')
    jwk_uri = well_known_res.json()['jwks_uri']
    logger.info("jwk_uri")
    logger.info(jwk_uri)
    jwk_res = requests.get(jwk_uri)
    jwk_keys = jwk_res.json()
    logger.info(jwk_keys)
    
    token_header = jwt.get_unverified_header(token)
    logger.info(token_header)
    x5c = None
    for key in jwk_keys['keys']:
        if key['kid'] == token_header['kid']:
            x5c = key['x5c']
            logger.info(x5c)
            break

    if x5c is None:
        raise Exception('Public key not found')

    cert = f"-----BEGIN CERTIFICATE-----\n{x5c[0]}\n-----END CERTIFICATE-----\n"
    cert = ''.join([
        '-----BEGIN CERTIFICATE-----\n',
        x5c[0],
        '\n-----END CERTIFICATE-----\n',
    ])

    logger.info(cert)

    public_key = load_pem_x509_certificate(cert.encode(), default_backend()).public_key()
    decoded_token = jwt.decode(
        token,
        public_key,
        algorithms=['RS256'],
        audience=audience,
        issuer=issuer
    )
    logger.info(decoded_token)
    return decoded_token