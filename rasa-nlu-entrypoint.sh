#!/bin/bash

set -e

apt-get update
apt-get install -y gettext-base

envsubst < /app/config_nlu_template.yml > /app/config_nlu.yml

exec "$@" 
