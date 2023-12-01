#!/usr/bin/python3
"""6-post_email"""
import requests
import sys


if __mame__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    req = requests.post(url, data)

    print("{}".format(req.text))
