#!/usr/bin/python3
""" A Python script that takes in a URL and an email, sends a
    POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8) """

if __name__ == "__main__":

    import urllib.request as url
    import urllib.parse as par
    import sys

    link = sys.argv[1]
    values = {'email' : sys.argv[2]}

    data = par.urlencode(values)
    data = data.encode('ascii')
    req = url.Request(link, data)
    with url.urlopen(req) as response:
        print(response.read().decode('utf-8'))
