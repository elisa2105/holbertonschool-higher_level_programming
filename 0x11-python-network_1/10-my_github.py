#!/usr/bin/python3
"""
request to github and display user id
"""

import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    pwd = argv[2]
    url = "https://api.github.com/users"
    req = requests.get(url, auth=(user, pwd))
    json = req.json()
    print("{}".format(json.get('id')))
