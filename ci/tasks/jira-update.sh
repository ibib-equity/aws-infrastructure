#!/bin/bash -e
echo $REPO_NAME
echo $BRANCH_SRC_NAME
echo $PR_NUMBER

BASEURL="jiraprod.duke-energy.com"
PATTERN="WDA-[0-9]+"

# Don't match on case
shopt -s nocasematch

# Check if jira pattern exists in the branch name
if [[ $BRANCH_SRC_NAME =~ $PATTERN ]]; then
  TICKET="${BASH_REMATCH[0]}"
  echo "Found jira ticket ref in branch $BRANCH_SRC_NAME as $TICKET"
else
  echo "No jira ticket found in branch name $BRANCH_SRC_NAME"
  exit 0
fi

COMMENT="PR created at https://github.com/dukeenergy-corp/$REPO_NAME/pull/$PR_NUMBER"
JIRA_RESP=$(curl -L \
   -X GET \
   -H "Authorization: Bearer $JIRA_CONCOURSE_TOKEN" \
   -H "Content-Type: application/json" \
   https://$BASEURL/rest/api/2/issue/$TICKET)

if (echo $JIRA_RESP | jq -e '.errorMessages') > /dev/null; then
  echo "JIRA issues for $TICKET does not exist"
else
  echo "Checking comments on JIRA issue $TICKET"
  COMMENTS_RESP=$(curl -L \
   -X GET \
   -H "Authorization: Bearer $JIRA_CONCOURSE_TOKEN" \
   -H "Content-Type: application/json" \
   https://$BASEURL/rest/api/2/issue/$TICKET/comment)

  if (echo $COMMENTS_RESP | jq -e ".comments[] | select(.body == \"$COMMENT\")" ) > /dev/null; then
    echo "Comment already exists"
  else
    echo "Comment does not exist, creating."
    curl -L \
     -X POST \
     -H "Authorization: Bearer $JIRA_CONCOURSE_TOKEN" \
     -H "Content-Type: application/json" \
     --data "{\"body\": \"$COMMENT\"}" \
     https://$BASEURL/rest/api/2/issue/$TICKET/comment > /dev/null
  fi
fi