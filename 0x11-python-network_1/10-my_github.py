#!/usr/bin/python3
""" A Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id """

if __name__ == "__main__":

    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    credentials = HTTPBasicAuth(username, password)
    req = requests.get("https://api.github.com/user", auth=credentials)
    print(req.json().get('id'))
