#!/bin/bash

if [ -z "$TOKEN" ]
then
    echo Set TOKEN
    exit 1
fi

ACTION=$1
NAME=$2
if [ -z "$NAME" -o -z "$ACTION" ]
then
    echo Usage ghtool.sh ACTION NAME
    exit 1
fi

if [ "$ACTION" = create ]
then
   curl -L -X POST -H "Authorization: Bearer $TOKEN" \
      https://api.github.com/orgs/big-data-team/repos \
      -d '{"name":"'$NAME'","description":""}'
elif [ "$ACTION" = delete ]
then
   curl -L -X DELETE -H "Authorization: Bearer $TOKEN" \
      https://api.github.com/repos/big-data-team/$NAME
else
    echo Incorrect action: $ACTION
fi
