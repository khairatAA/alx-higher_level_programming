#!/usr/bin/python3
"""100-github_commits module"""
import requests
import sys


if __name__ == "__main__":
    """
    You must use the GitHub API, here is the documentation
    https://developer.github.com/v3/repos/commits/
    """

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = ('https://api.github.com/repos/{}/{}/commits').format(
            owner_name,
            repo_name
            )

    response = requests.get(url)

    if response.status_code == 200:
        json = response.json()[:10]
        for i in json:
            print("{}: {}".format(
                json[i].get("sha"),
                json[i].get("commit").get("author").get("name")
                ))
