#!/usr/bin/bash

USER=big-data-team
REP_NAME="$1"

# check args
if [ -z "$REP_NAME" ]
then
    echo Usage: `basename $0` REPOSITORY_NAME
    exit 1
fi

if [ -z "$TOKEN" ]
then
    echo Set env variable TOKEN to github token
    exit 1
fi

# check if rep exist
REP_ID=`curl -s -H "Authorization: Bearer $TOKEN" https://api.github.com/repos/$USER/$REP_NAME | jq '.id'`
if [ "$REP_ID" == "null" ]
then
    EXIST=0
else
    EXIST=1
fi

if [ "$EXIST" == 0 ]
then
    # create
    echo creating $USER/$REP_NAME
    curl -s -X POST -H "Authorization: Bearer $TOKEN" https://api.github.com/orgs/$USER/repos -d "{\"name\": \"$REP_NAME\", \"description\": \"The test github API\"}" -H "Content-Type: applicaton/json"
else
    # delete
    echo deleting $USER/$REP_NAME
    echo curl -s -X DELETE -H "Authorization: Bearer $TOKEN" https://api.github.com/repos/$USER/$REP_NAME
fi
