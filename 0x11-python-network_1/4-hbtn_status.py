#!/usr/bin/python3
""" A Python script that takes fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":

    import requests

    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
