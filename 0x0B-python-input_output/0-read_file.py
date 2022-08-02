#!/usr/bin/python3


"""
A module that has a function to read a file
"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
