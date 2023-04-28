#!/usr/bin/python3
""" A Python script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter. """

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        letter = ""
    elif len(sys.argv) == 2:
        payload = {'q': letter}

    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        res = req.json()
        if res == {}:
            print("No result") if res == {}
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print("Not a valid JSON")
