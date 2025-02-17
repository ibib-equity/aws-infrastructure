#!/bin/bash -e
duke-install awscli 2.2.4

echo "aws version"
aws --version
bash --version
echo $SHELL
# Exit on error

apt-get -qq update
apt-get install -qq -y python3.9 python3-pip zip

echo "python version"
python3.9 --version

echo "pip version"
pip --version

export AWS_REGION=${region}
echo "Region set to: ${region}"

echo "Setting AWS access tokens"
export AWS_ACCESS_KEY_ID=`cat secrets/access_key`
export AWS_SECRET_ACCESS_KEY=`cat secrets/secret_key`
export AWS_SESSION_TOKEN=`cat secrets/security_token`
echo "Successfully set AWS access tokens"

pushd src/src

functions=$(aws lambda list-functions --query 'Functions[*].[FunctionName]' --output text)
# shellcheck disable=SC2068
for function_name in ${functions[@]} ; do
  directory=$(echo "${function_name}" | sed -r "s:data-catalog-::g" | sed -r "s:${environment_suffix}::g" | sed -r 's:-:_:g')
  echo "Starting processing of ${directory}"
  if [ -d "${directory}" ]; then
    echo "${directory} exists, changing into it..."
    cd "${directory}"
    if [ -f requirements.txt ];then
        echo "Found requirements.txt & installing pip requirements..."
        pip3 install --target . -r requirements.txt # pip install requirements
    fi
    zip -r -q -T "${directory}".zip *
    zip="${directory}.zip"
    echo "updating ${function_name} code with ${zip}..."
    aws --no-verify-ssl lambda update-function-code \
    --function-name "${function_name}" \
    --zip-file "fileb://${zip}" > /dev/null || :
    cd ..
  else
    echo "${directory} does not exist in list of lambda directories..."
    continue
  fi
done
