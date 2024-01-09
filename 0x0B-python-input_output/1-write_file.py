#!/usr/bin/python3
"""Module contain write_file(filename="", text="") func"""


def write_file(filename="", text=""):
    """
    a function that writes a string
    to a text file (UTF8) and returns the number
    of characters written:

    args: filename: name of the file
          text: text to be written
    return: number of characters written:
    """
    with open(filename, 'w', encoding='UTF8') as file:
        char_written = file.write(text)
        return char_written
