#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":

    import urllib.request as url

    with url.urlopen('https://alx-intranet.hbtn.io/status') as response:
        page = response.read()

        print('Body response:')
        print('\t- type:', type(page))
        print('\t- content:', page)
        print('\t- utf8 content:', page.decode('utf-8'))
