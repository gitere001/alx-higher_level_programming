#!/bin/bash
# script to get size of http response header
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -s "$1" | wc -c
