#!/usr/bin/python3
"""3-error_code"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    """
    That takes in a URL, sends a request to the URL
    and displays the body of the response
    """
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            resp = response.read()
            html = resp.decode("UTF-8")
            print("{}".format(html))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
