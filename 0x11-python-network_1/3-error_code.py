#!/usr/bin/python3
"""manage HTTPError"""
import urllib.error
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print((response.read()).decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
