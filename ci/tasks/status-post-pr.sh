#!/bin/bash -e
echo "Setting status for $REPO_NAME/pulls/$PR_NUMBER to $STATUS with description '$DESCRIPTION'"

echo $ATC_EXTERNAL_URL
echo $PIPELINE_NAME
echo $INSTANCE_VARS
echo $PRODUCT_NAME

PR_RESPONSE=$(curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_CONCOURSE_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/dukeenergy-corp/$REPO_NAME/pulls/$PR_NUMBER)

STATUS_HREF=$(echo $PR_RESPONSE | jq -r '._links.statuses.href')
echo $STATUS_HREF

for r in $INSTANCE_VARS; do
  IFS='='
  read -ra newarr <<< "$r"
  prefix=$(printf "${newarr[0]}")
  suffix=$(printf "\"${newarr[1]}\"" | jq -sRr @uri)
  IFS=''
  url_params+="&vars.$prefix=$suffix"
done

url_params=$(echo $url_params | cut -c 2-)

target_url="${ATC_EXTERNAL_URL}/teams/${PRODUCT_NAME}/pipelines/${PIPELINE_NAME}?$url_params"
echo $target_url

curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_CONCOURSE_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "$STATUS_HREF" \
  -d "{\"state\":\"$STATUS\",\"target_url\":\"$target_url\",\"description\":\"$DESCRIPTION\",\"context\":\"continuous-integration/concourse\"}"
