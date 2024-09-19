#!/usr/bin/bash

FILE_TO_WORK=$1

if [ -f "$FILE_TO_WORK" ]; then
    echo "file exists"
else
    echo "usage: $0 <file>"
    exit 1
fi
