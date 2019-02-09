#!/bin/bash

set -e

envsubst < /app/endpoints_template.yml > /app/endpoints.yml
envsubst < /app/credentials_template.yml > /app/credentials.yml

exec "$@" 
