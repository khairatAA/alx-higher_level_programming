#!/usr/bin/python3
"""8-json_api"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1]

    if letter = "":
        data = {'q': ""}
    else:
        data = {'q': letter}

    resp = requests.get(url)

    try:
        to_dict = resp.json()

        if to_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(to_dict["id"], to_dict["name"]))
    except ValueError:
        print("Not a valid JSON")
