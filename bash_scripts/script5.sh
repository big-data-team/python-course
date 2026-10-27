#!/bin/bash


for x in $(seq $1)
do
    echo hello >text$x.txt
done