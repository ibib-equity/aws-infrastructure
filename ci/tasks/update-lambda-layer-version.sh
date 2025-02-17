#!/bin/bash -e
duke-install awscli 2.4.16

export AWS_REGION=${region}
echo "Region set to: ${region}"

echo "Setting AWS access tokens"
export AWS_ACCESS_KEY_ID=`cat secrets/access_key`
export AWS_SECRET_ACCESS_KEY=`cat secrets/secret_key`
export AWS_SESSION_TOKEN=`cat secrets/security_token`
echo "Successfully set AWS access tokens"

# Add in the layers in an output file
echo "Layers to deploy"
export layer_arn=`cat layer_info/layer_arn`
export layer_version_arn=`cat layer_info/layer_version_arn`

# Apply the layer version update
functions=$(aws lambda list-functions --query 'Functions[*].[FunctionName]' --output text)
# shellcheck disable=SC2068
for function_name in ${functions[@]} ; do
  runtime=$(aws lambda get-function-configuration --function-name "$function_name" --query 'Runtime' --output text)
  if [[ $runtime == "python3."* ]]; then
    echo "Applying $layer_version_arn to ${function_name}"
    aws lambda update-function-configuration \
      --function-name "${function_name}" \
      --layers "${layer_version_arn}"
  else
    echo "Skipping non-Python Lambda: $function_name (Runtime: $runtime)"
  fi
done
