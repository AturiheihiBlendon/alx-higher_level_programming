#!/usr/bin/python3


"""
A module that has a function to print
a square with character "#"
"""


def print_square(size):
    """
    Function to print a square with
    character "#"
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
