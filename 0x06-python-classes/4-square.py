#!/usr/bin/python3
'''Defining a class Square Defined by size'''


class Square:
    '''Defines a square'''

    def __init__(self, size=0):
        '''
        Initializes a square
        Args:
            size: size of the square
        '''
        self.size = size

    @property
    def size(self):
        '''retreive the size of the square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''define the area of the square'''
        return(self.__size**2)
