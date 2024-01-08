#!/usr/bin/python3

"""A module with a function that a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list
    """
    def print_sorted(self):
        """prints a sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
