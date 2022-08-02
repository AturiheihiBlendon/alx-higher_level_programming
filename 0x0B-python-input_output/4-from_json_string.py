#!/usr/bin/python3

"""
A module that has a JSON-to-object function
"""
import json


def from_json_string(my_str):
    """A function that return the
    Python object representation of a JSON string.
    """
    return json.loads(my_str)
