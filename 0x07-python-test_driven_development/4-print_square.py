#!/usr/bin/python3

"""Defining a function that prints square with #"""


def print_square(size):
    """A function that prints square with #

    argrs:
         size: (int) size of the square
    raises:
         TypeError: if size is not int
         ValueError: if size is less than zero
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print('#' * size)
