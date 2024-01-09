#!/usr/bin/python3
"""Module containing append_write(filename="", text=""):"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the
    end of a text file (UTF8) and returns the number of
    characters added

    Args: filename(str): name of the file to be appended
          text(str): string added

    Return: number of character added
    """
    with open(filename, 'a', encoding='utf8') as file:
        appended_char = file.write(text)
        return appended_char
