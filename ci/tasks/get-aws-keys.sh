#!/bin/bash
duke-install vault 1.7.1
vault version

# exit script on error
set -e

vault login -field=token \
  -address=${vault_url} \
  -tls-skip-verify \
    token=${vault_token}
  > /dev/null

vault write \
  -address=${vault_url} \
  -tls-skip-verify \
  -format json \
  aws/${aws_account_id}/sts/automation.code.role ttl=60m \
  > secrets/keys.json

jq -r .data.access_key < secrets/keys.json > secrets/access_key
jq -r .data.secret_key < secrets/keys.json > secrets/secret_key
jq -r .data.security_token < secrets/keys.json > secrets/security_token