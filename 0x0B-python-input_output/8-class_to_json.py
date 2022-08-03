#!/usr/bin/python3


"""
A module that has a function to return
A function to return the dictionary
represntation of a simple data structure
"""


def class_to_json(obj):
    """A function to return the dictionary
    represntation of a simple data structure
    """
    return obj.__dict__
