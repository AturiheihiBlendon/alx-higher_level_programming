#!/usr/bin/python3


"""
A module that has a function to write
to a file
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
