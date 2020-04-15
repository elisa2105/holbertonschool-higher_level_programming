#!/usr/bin/python3
""" Displays the body utf-8 """
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {"email": argv[2]}
    with urlopen(url, urlencode(email).encode()) as response:
        print(response.read().decode("utf-8"))
