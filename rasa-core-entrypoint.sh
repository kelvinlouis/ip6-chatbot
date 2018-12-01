#!/bin/bash

set -e

apt-get update
apt-get install -y gettext-base

envsubst < /app/endpoints_template.yml > /app/endpoints.yml
envsubst < /app/credentials_template.yml > /app/credentials.yml

exec "$@" 
