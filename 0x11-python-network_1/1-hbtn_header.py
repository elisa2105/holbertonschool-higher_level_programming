#!/usr/bin/python3
"""displays the X-reuqest-Id"""
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url = argv[1]
    with urlopen(url) as response:
        page = response.headers.get("X-request-Id")
        print(page)
