#!/bin/bash -e

APP="github-pullrequests-setter"
TEAM="data-catalog"

echo -e -n "1. sandbox
2. dev
3. qa
4. prod
5. force check all resources
? [\033[36m3\033[0m]: "
read ENV

ENV=${ENV:-3}

# pipeline-setter = the MAIN pipeline. pipeline-template-master / prs = the SPAWNED pipelines (not used here).
PIPELINE_CONFIG="pipelines/pipeline-setter.yml"

case "$ENV" in
    1) TARGET=dt; NAME=sbx ;;
    2) TARGET=dt; NAME=dev ;;
    3) TARGET=qa; NAME=qa ;;
    4) TARGET=prod; NAME=prod ;;
esac

set -x
fly -t "${TARGET}-${TEAM}" sync
fly -t "${TARGET}-${TEAM}" set-pipeline \
    --pipeline "${APP}" \
    -c "$PIPELINE_CONFIG" \
    --load-vars-from "config/parameters-pr-setting-config.yml"

fly -t "${TARGET}-${TEAM}" hide-pipeline --pipeline "${APP}"
set +x

echo -e "\n\n - TO UNHIDE:"
echo "   $ fly -t ${TARGET}-${TEAM} expose-pipeline --pipeline ${APP}"
echo " - TO DELETE:"
echo "   $ fly -t ${TARGET}-${TEAM} destroy-pipeline --pipeline ${APP}"
