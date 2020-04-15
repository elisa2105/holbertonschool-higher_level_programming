#!/usr/bin/python3
"""request a website"""
from urllib.request import urlopen
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urlopen(url) as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
