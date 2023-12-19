#!/usr/bin/python3
"""A module for square"""


class Square:
    """Represent a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
