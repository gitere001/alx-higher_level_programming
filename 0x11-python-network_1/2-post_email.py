#!/usr/bin/python3
"""
ython script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    encoded_data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, encoded_data)
    with urllib.request.urlopen(request) as response:
        data = response.read().decode("utf-8")
        print(data)
