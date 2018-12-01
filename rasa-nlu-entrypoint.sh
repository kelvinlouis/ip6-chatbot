#!/bin/bash

set -e

apt-get update
apt-get install -y gettext-base

wget -N "https://anaconda.org/intel/tensorflow/1.10.0/download/tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl-avx2.whl"
pip install -U "tensorflow-1.10.0-cp36-cp36m-linux_x86_64.whl-avx2.whl"

if [ -f /app/config_nlu_template.yml ]; then
  envsubst < /app/config_nlu_template.yml > /app/config_nlu.yml
fi

exec "$@" 
