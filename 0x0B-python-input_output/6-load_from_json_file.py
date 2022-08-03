#!/usr/bin/python3


"""
A module that has a function to create an
object from a JSON
"""
import json


def load_from_json_file(filename):
    """A function to create an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
