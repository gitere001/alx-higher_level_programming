#!/usr/bin/python3
"""Module contain a class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle"""
    def __init__(self, size,  x=0, y=0, id=None):
        """Class constructor for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set width of a square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the square
        *args (integers): value of new attributes
               1st arg is id
               2nd arg is size
               3rd arg is x
               4th arg is y
        **kwargs (dict): new key and values of attributes

        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y

        }
