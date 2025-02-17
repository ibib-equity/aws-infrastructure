#!/bin/bash -e

docker-compose up -d
sleep 2
docker exec -it dc bash -c "cd /code/src; python3.11 -m unittest discover -v shared"
docker exec -it dc bash -c "cd /code/src/collibra_api_integration; python3.11 -m unittest tests/test_collibra_api_integration.py -v"
docker exec -it dc bash -c "cd /code/src/corp_kafka_sink_connector; python3.11 -m unittest tests/test_individual_kafka_sink_connector_functions.py"
docker exec -it dc bash -c "cd /code/src/nuc_kafka_sink_connector; python3.11 -m unittest tests/test_individual_kafka_sink_connector_functions.py"

docker-compose down
