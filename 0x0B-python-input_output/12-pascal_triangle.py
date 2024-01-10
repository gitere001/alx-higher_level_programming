#!/usr/bin/python3
"""A module containing pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s
    triangle of n.

    Args:
    - n (int): the number of rows in the Pascal triangle.

    Returns:
    - List[List[int]]: A list of lists representing Pascal's Triangle.
      Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize the Pascal's Triangle
    result = [[1] * i for i in range(1, n + 1)]

    # Populate the triangle based on the rules
    for i in range(2, n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    return result
