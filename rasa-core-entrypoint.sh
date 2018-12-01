#!/bin/bash

set -e

apt-get update
apt-get install -y gettext-base netcat

pip install -U "/app/pip-cache/tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl-avx2.whl"

envsubst < /app/endpoints_template.yml > /app/endpoints.yml
envsubst < /app/credentials_template.yml > /app/credentials.yml

echo "Waiting for rasa-nlu..."

while ! nc -z rasa-nlu 5000; do   
  sleep 0.5 # wait for 1/10 of the second before check again
done

echo "rasa-nlu launched"

exec "$@" 
