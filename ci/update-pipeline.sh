#!/bin/bash -e

APP="dm"
TEAM="data-catalog"

echo -e -n "1. sandbox
2. dev
3. qa
4. prod
5. force check all resources
? [\033[36m3\033[0m]: "
read ENV

ENV=${ENV:-3}

PIPELINE_CONFIG="pipelines/pipeline.yml"

case "$ENV" in
    1) TARGET=dev; NAME=sbx ; PIPELINE_CONFIG="pipelines/pipeline-with-tests.yml" ;;
    2) TARGET=dev; NAME=dev ; PIPELINE_CONFIG="pipelines/pipeline-with-tests.yml" ;;
    3) TARGET=qa; NAME=qa; PIPELINE_CONFIG="pipelines/pipeline-with-tests.yml" ;;
    4) TARGET=prod; NAME=prod; PIPELINE_CONFIG="pipelines/pipeline-with-tests.yml" ;;
    5)
        echo -e "NOTE: if any of these error, it may not actually be an issue.\n"
        for ENV in sbx tst dev qa;do

            resources=$(fly -t "${TARGET}-${TEAM}" get-pipeline -p "build-${APP}-${ENV}" | grep -B2000 "^jobs:" | sed -r -n "s:^- name\: (.*):\1:p")
            for rsc in $resources;do
                (set -x; fly -t "${TARGET}-${TEAM}" check-resource --resource "build-${APP}-${ENV}/${rsc}")
            done
        done
        exit 0 ;;
    "") TARGET=dt; NAME=dev ;;
    *) echo -e "\033[31merror:\033[0m Unknown environment, $ENV. Select 1-6."; exit 1 ;;
esac

set -x
fly -t "${TARGET}-${TEAM}" sync
fly -t "${TARGET}-${TEAM}" set-pipeline \
    --pipeline "build-${APP}-${NAME}" \
    -c "$PIPELINE_CONFIG" \
    --load-vars-from "config/parameters-${NAME}.yml" \
    --load-vars-from "config/parameters-common.yml"

fly -t "${TARGET}-${TEAM}" hide-pipeline --pipeline "build-${APP}-${NAME}"
set +x

echo -e "\n\n - TO UNHIDE:"
echo "   $ fly -t ${TARGET}-${TEAM} expose-pipeline --pipeline build-${APP}-${NAME}"
echo " - TO DELETE:"
echo "   $ fly -t ${TARGET}-${TEAM} destroy-pipeline --pipeline build-${APP}-${NAME}"
