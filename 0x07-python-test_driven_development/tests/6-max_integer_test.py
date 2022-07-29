#!/usr/bin/python3


"""
A module that has unittests for a function to find
and return max integer in a list of integers
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class defining test max integer"""

    def test_ordered_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        string = "Men"
        self.assertEqual(max_integer(string), 'n')

    def test_list_of_strings(self):
        strings = ["Are", "you", "there", "please"]
        self.assertEqual(max_integer(strings), "you")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
