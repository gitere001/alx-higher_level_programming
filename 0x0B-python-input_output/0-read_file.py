#!/usr/bin/python3

"""Module having a function read_file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            print(line, end='')
