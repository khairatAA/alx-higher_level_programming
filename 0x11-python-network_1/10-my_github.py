#!/usr/bin/python3
"""10-my_github"""
import requests
import sys


if __name__ == "__main__":
    """
    Takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
    """

    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)
    response = requests.get('https://api.github.com/user', auth=auth)

    if response.status_code == 200:
        json = response.json()
        print(json["id"])
    else:
        print("None")
