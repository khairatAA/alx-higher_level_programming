#!/usr/bin/python3
"""8-json_api"""
import requests
import sys


if __name__ == "__main__":
    """Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
    """

    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv[1]) >= 1:
        letter = sys.argv[1]
    else:
        letter = None

    if letter is not None:
        data = {'q': letter}
    else:
        data = {}

    try:
        resp = requests.post(url, data=data)
        to_dict = resp.json()

        if to_dict:
            print("[{}] {}".format(to_dict["id"], to_dict["name"]))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
