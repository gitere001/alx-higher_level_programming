#!/usr/bin/python3
"""Inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle with inhertance BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_vaidator('height', height)
        self.__height = height
