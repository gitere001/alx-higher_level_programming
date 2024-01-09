#!/usr/bin/python3

"""Module containing load_from_json_file(filename) function"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
