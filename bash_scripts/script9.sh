#!/usr/bin/bash

N=10 # "$1"

A=1
while [ "$A" -le "$N" ]; do
    echo $A
    A=$[$A + 1]
done

