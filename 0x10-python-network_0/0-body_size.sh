#!/usr/bin/env bash
# A Bash script that takes in a URL,displays the size of the response in bytes
curl -s "$1" | wc -c
