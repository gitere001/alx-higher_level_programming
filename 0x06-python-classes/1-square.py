#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square with a private size attribute."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
