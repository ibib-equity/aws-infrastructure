#!/bin/bash
duke-install awscli 2.4.16

apt-get update
apt-get upgrade
apt-get install -y -qq python3.11 python3.11-venv
apt-get install -y -qq zip

# Exit on error
set -e

TASK_BASE_DIR="$PWD"

export AWS_REGION=${region}
echo "Region set to: ${region}"

echo "Setting AWS access tokens"
export AWS_ACCESS_KEY_ID=`cat secrets/access_key`
export AWS_SECRET_ACCESS_KEY=`cat secrets/secret_key`
export AWS_SESSION_TOKEN=`cat secrets/security_token`
echo "Successfully set AWS access tokens"

pushd src/src/shared
ls

echo "Creating Virtual Environment"
python3.11 -m venv .
source bin/activate
echo "Installing pip"
apt-get install -y -qq python3-pip
echo "Installing poetry"
curl -sSL https://install.python-poetry.org |python3.11 - --version 1.2.0
export PATH="/root/.local/bin:$PATH"
echo "Building the wheel"
poetry build
echo "Installing the wheel"
pip3 install dist/shared-0.1.0-py3-none-any.whl

mkdir python
ls lib/python3.11/site-packages/
mv lib/python3.11/site-packages/* python
zip -r -qq ./python.zip python
ls

# Update the request layer
layer_name="shared-layer"
echo "updating ${layer_name} code"
response=$(aws lambda publish-layer-version --layer-name $layer_name \
  --compatible-runtimes "python3.11" --compatible-architectures "x86_64" --zip-file "fileb://python.zip")
layer_arn=$(echo "$response" | jq -r '.LayerArn')
layer_version_arn=$(echo "$response" | jq -r '.LayerVersionArn')
popd
ls

# Add in the layer info into specific layers
echo "$layer_arn" >> layer_info/layer_arn
echo "$layer_version_arn" >> layer_info/layer_version_arn
