#!/usr/bin/python3
"""module contain save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj (object): The Python object to be written.
        filename (str): The name of the file to write the JSON data to.
    """
    with open(filename, 'w') as json_file:
        json.dump(my_obj, json_file)
