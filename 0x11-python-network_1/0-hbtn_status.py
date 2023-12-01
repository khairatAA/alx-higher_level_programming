#!/usr/bin/python3
"""0-hbtn_status module"""
import urllib.request

if __name__ == "__main__":
    """
     fetches https://alx-intranet.hbtn.io/status
     """

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        resp = response.read()

        url_type = type(resp)
        html = resp.decode("UTF-8")

        print("Body response:")
        print("\t- type: {}".format(url_type))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(html))
