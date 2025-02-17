#!/bin/bash -e

apt-get update
apt-get install -y -qq python3.11 python3-pip

echo "Checking the contents of the src directory"
ls source-repo
echo "Changing directory into the src directory"
cd source-repo

pip install -r requirements.txt

cd src
python3 -m unittest discover -v shared

cp shared/shared.py collibra_api_integration
cd collibra_api_integration
python3 -m unittest tests/test_collibra_api_integration.py
cd ..
