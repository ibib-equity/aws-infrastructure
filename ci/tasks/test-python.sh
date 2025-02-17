#!/bin/bash -e

apt-get update
apt-get install -y -qq python3.11 python3-pip

echo "Checking the contents of the src directory"
ls src
echo "Checking the contents of the artifacts directory"
ls artifacts
echo "Changing directory into the src directory"
cd src

pip install -r requirements.txt
python3 -m unittest discover -v src/shared/
