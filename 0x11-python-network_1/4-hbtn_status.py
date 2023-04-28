#!/usr/bin/python3
""" A Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8). """

if __name__ == "__main__":

    import urllib.request as url
    import urllib.error as err
    import sys

    link = sys.argv[1]

    req = url.Request(link, data)
    try:
        with url.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except err.HTTPError as e:
        print('Error code:', e.code)
