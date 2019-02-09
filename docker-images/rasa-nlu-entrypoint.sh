#!/bin/bash

set -e

if [ -f /app/config_nlu_template.yml ]; then
  envsubst < /app/config_nlu_template.yml > /app/config_nlu.yml
fi

exec "$@" 
