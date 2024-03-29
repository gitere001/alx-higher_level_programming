#!/usr/bin/python3
"""
ython script that fetches https://alx-intranet.hbtn.io/status
using requests packages
"""
import requests
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    body = requests.get(url)
    print("Body response")
    print(f"\t- type: {type(body.text)}")
    print(f"\t- content: {body.text}")
