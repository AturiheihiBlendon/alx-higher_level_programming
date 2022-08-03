#!/usr/bin/python3


"""
A module that has definition of a student class
and a function to return a dictionary
representation of the Student
"""


class Student:
    """A class to represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A function to return a dictionary
        representation of the Student
        """
        return self.__dict__
