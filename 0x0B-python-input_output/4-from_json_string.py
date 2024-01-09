#!/usr/bin/python3

"""Module contain def from_json_string(my_str):"""

import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure)
    represented by a JSON string:

    args: my_str(str): string to be converted to string from jason

    return: object (Python data structure) represented by a JSON string:
    """
    return json.loads(my_str)
