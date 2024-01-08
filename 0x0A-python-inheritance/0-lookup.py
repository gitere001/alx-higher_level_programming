#!/usr/bin/python3

"""module with a function that returns the list of available
attributes and methods of an object:"""


def lookup(obj):
    """a function that returns the list of available
    attributes and methods of an object
    Args:
       obj: Object for which attributes and methods are retrieved.

    Return: a list object
    """
    return dir(obj)
