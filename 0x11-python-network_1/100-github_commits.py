#!/usr/bin/python3
"""A WILD COMMENT APPEARS"""


if __name__ == "__main__":
    from sys import argv
    import requests

    url, owner, repo = "https://api.github.com/repos/", argv[2], argv[1]

    connect = requests.get(url + owner + '/' + repo + '/commits')
    response = connect.json()[:10]

    for dicts in response:
        print(dicts['sha'] + ': ' + dicts['commit']['author']['name'])
