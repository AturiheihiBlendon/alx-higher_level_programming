#!/usr/bin/python3


"""
Module that has a function to print first and last name
passed to it
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print first and las name passed to it
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
