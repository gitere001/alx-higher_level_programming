#!/bin/bash
# script to get size of http response header
curl -s "$1" | wc -c
