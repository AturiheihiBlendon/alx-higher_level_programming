#!/usr/bin/python3

"""A module that has a function to look up
an object's attributes and methods
"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
