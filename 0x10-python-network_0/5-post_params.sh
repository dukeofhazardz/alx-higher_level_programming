#!/bin/bash
# A Bash script that takes in a URL, sends a POST request, displays response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
