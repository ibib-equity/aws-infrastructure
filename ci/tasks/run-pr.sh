#!/bin/bash -e
echo $REPO_NAME
echo $BRANCH_DEST_NAME
echo $BRANCH_SRC_NAME

echo "Running against branch $BRANCH_SRC_NAME in $REPO_NAME"

# base directory in the container where this task starts from (where inputs/outputs are).
export TASK_BASE_DIR="$PWD"

echo "Executing pre merge in $REPO_NAME"
"./source-repo/ci/tasks/run-pre-merge.sh" || exit 1
echo "Task complete"
