#!/usr/bin/python3

"""
A module that has a function to append
to a file
"""


def append_write(filename="", text=""):
    """
    A function that appends to a file
    """
    with open("filename", "a", encoding="UTF8") as f:
        return f.write(text)
