#!/usr/bin/python3
"""1-hbtn_header module"""
import sys
import urllib.request


if __name__ == "__main__":
    """
    takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id
    variable found in the header of the response
    """

    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        resp = response.getheader("X-Request-Id")

        print("{}".format(resp))
