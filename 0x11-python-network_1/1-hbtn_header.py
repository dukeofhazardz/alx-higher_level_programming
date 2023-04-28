#!/usr/bin/python3
""" A Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable found in
    the header of the response. """

if __name__ == "__main__":

    import urllib.request as url
    import sys

    link = sys.argv[1]
    #req = url.Request(link)
    with url.urlopen(link) as response:
        print(dict(response.headers).get('X-Request-Id'))
