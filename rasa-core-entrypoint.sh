#!/bin/bash

set -e

apt-get update
apt-get install -y gettext-base netcat

envsubst < /app/endpoints_template.yml > /app/endpoints.yml
envsubst < /app/credentials_template.yml > /app/credentials.yml

echo "Waiting for rasa-nlu..."

while ! nc -z rasa-nlu 5000; do   
  sleep 0.1 # wait for 1/10 of the second before check again
done

echo "rasa-nlu launched"

exec "$@" 
