#!/usr/bin/python3
"""
get the X-Request-Id using requests
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
