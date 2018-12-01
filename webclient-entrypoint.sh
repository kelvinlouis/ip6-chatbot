#!/bin/bash

# Source: https://gist.github.com/mauvm/5de07085f3b51e117378#gistcomment-2248266
# NOTE: Brackets are not supported and '$' in values will break the script.

function replace_env {
  mkdir /etc/nginx/conf.d 2> /dev/null
  cp -rf /app/conf/. /etc/nginx/conf.d/
  for file in /etc/nginx/conf.d/*.conf
  do
    TPL=$(cat $file)
    for row in $(env)
    do
      SAVEIFS=$IFS
      IFS="="
      read key val <<< "$row"
      IFS=$SAVEIFS
      if [[ $val == tcp://* ]]
      then
        valhttp=$(echo -n $val | sed 's#^tcp://#http://#')
        TPL=$(echo -n $TPL | sed "s\$\\\$$key\_HTTP\$$valhttp\$")
      else
        TPL=$(echo -n $TPL | sed "s\$\\\$$key\$$val\$")
      fi
    done
    echo -n $TPL > "/etc/nginx/conf.d/$(basename $file)"
  done
}

replace_env
nginx -g "daemon off;"