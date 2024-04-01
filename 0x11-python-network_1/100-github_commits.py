#!/usr/bin/python3
""" python script that takes 2 arguments in order to solve this challenge;
'Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line).'

The first argument will be the repository name
The second argument will be the owner name
uses packages requests and sys
"""
from sys import argv
import requests

if __name__ == "__main__":
    repo_name = argv[1]
    owner_name = argv[2]
    url = (f'https://api.github.com/repos/{owner_name}/'
           f'{repo_name}/commits')

    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits. Please check the repository and owner "
              "names.")
