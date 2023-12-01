#!/usr/bin/python3
"""7-error_code"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get('url')

    if response.code >= 400:
        print("Error code: {}".format(response.code))