#!/bin/bash -e

echo "Please make sure you're using the most recent version of fly"
TEAM="data-catalog"

URI=""

while true;do
    echo -e -n "which concourse environment would you like to set?:
 1. dev/tst
 2. qa
 3. prod
 ?[\033[36m1\033[0m]: "
    read ENV

	ENV=${ENV:-1}

    case "$ENV" in
        "1") URI=dev; break ;;
        "2") URI=qa; break ;;
        "3") URI=prod; break ;;
        *) echo -e "\033[31merror:\033[0m Unknown environment, $ENV. Select 1-3."; exit 1 ;;
    esac
done

set -x
fly -t "${URI}-${TEAM}" login --team-name "${TEAM}" --concourse-url "https://concourse-${URI}.ci.duke-energy.app"
fly -t "${URI}-${TEAM}" sync
