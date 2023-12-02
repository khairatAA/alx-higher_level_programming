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

    letter = sys.argv[1]

    if len(letter) == 0:
        letter = ""
    elif len(letter) == 1:
        letter = sys.argv[1]

    data = {'q': letter}

    resp = requests.post(url, data=data)

    try:
        to_dict = resp.json()

        if to_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(to_dict["id"], to_dict["name"]))
    except ValueError:
        print("Not a valid JSON")
