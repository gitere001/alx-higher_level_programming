#!/usr/bin/python3

"""module containing a class student"""


class Student:
    """ a class having;
    Public instance attributes:
    first_name
    last_name
    age
    def to_json(self):
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
