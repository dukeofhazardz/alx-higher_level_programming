#!/bin/bash
# A Bash script that takes a URL and displays HTTP methods the server accepted.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
