#!/usr/bin/python3
""" A Python script that takes 2 arguments in order
    to solve this challenge. """

if __name__ == "__main__":

    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repo_name)

    req = requests.get(url)
    the_commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(the_commits[i].get("sha"), the_commits[i]
                                  .get("commit").get("author").get("name")))
    except IndexError:
        pass
