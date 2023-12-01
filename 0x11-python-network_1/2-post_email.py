#!/usr/bin/python3
"""2-post_email module"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    """
    Takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and
    displays the body of the response
    """
    url = sys.argv[1]
    email_address = sys.argv[2]

    value = {'email': email_address}

    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        resp = response.read()

        html = resp.decode("UTF-8")
        print("{}".format(html))
