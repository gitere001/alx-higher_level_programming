#!/usr/bin/python3

"""A module containing class_to_json(obj)"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with a
    simple data structure
    (list, dictionary, string, integer, and boolean)
    for JSON serialization of an object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError(f"{obj} is not serializable.")

    serializable_attributes = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes
