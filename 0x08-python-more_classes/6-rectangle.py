#!/usr/bin/python3
""" Defining a rectangle class"""


class Rectangle:
    """ Represent a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        P_rectangle = []
        for i in range(self.__height):
            [P_rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                P_rectangle.append("\n")
        return ("".join(P_rectangle))

    def __repr__(self):
        P_rectangle = "Rectangle(" + str(self.__width)
        P_rectangle += ", " + str(self.__height) + ")"
        return (P_rectangle)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
