#!/usr/bin/python3
"""get id github """

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    if len(sys.argv) > 1:
        user = sys.argv[1]
        pwd = sys.argv[2]

    r = requests.get(url, auth=(user, pwd))
    json = r.json()
    print("{}".format(json.get('id')))
