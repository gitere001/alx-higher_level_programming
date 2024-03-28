#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak value from the list, which is greater than or equal
        to its neighbors.
             Returns None if the input list is empty or None.

    Note:
        A peak value is defined as an integer that is greater than or
        equal to its adjacent values.
    """

    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
