#!/usr/bin/python3
"""4-hbtn_status module"""
import requests


if __name__ == "__main__":
    """
    Python script that fetches https://alx-intranet.hbtn.io/status
    """

    response = requests.get('https://alx-intranet.hbtn.io/status')

    response_type = type(response.text)

    print("Body response:")
    print("\t- type: {}".format(response_type))
    print("\t- content: {}".format(response.text))
