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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''define the area of the square'''
        return(self.__size**2)
