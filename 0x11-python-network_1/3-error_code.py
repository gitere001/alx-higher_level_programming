#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
