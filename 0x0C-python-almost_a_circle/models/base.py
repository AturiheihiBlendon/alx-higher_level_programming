#!/usr/bin/python3


"""
A module that defines a base class
"""


class Base:
    """
    Represent a base class
    Attributes:
        __nb_objects (int): counts the number of objects created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        Args:
            id (int): The Id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
