#!/usr/bin/python3
import json


"""A module that has a string-to-JSON function."""


def to_json_string(my_obj):
    """ A function to return the JSON
    representation of a string object"""
    return json.dumps(my_obj)
