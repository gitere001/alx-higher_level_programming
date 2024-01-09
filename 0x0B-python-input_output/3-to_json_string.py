#!/usr/bin/python3

"""Module contain def to_json_string(my_obj) func"""
import json


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string):
    arg: my_obj(object): the python object to be converted to json

    return: JSON representation of an object (string)
    """
    json_string = json.dumps(my_obj)
    return json_string
