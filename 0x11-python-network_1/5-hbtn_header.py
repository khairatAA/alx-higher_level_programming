#!/usr/bin/python3
"""5-hbtn_header module"""
import requests
import sys


if __name__ == "__main__":
    """
    Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the variable X-Request-Id
    in the response header
    """
    url = sys.argv[1]

    response = requests.get(url)

    X_Request_Id = response.headers.get('X-Request-Id')
    print("{}".format(X_Request_Id))
