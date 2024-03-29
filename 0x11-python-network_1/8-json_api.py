#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests

if __name__ == "__main__":
    letter = argv[1] if len(argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_response = response.json()
        if json_response == {}:
            print("No result")
        else:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")

    except ValueError:
        print("Not a valid JSON")
