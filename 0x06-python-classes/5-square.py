#!/usr/bin/python3
"""Square Class"""


class Square:
    """Initializing a square"""
    def __init__(self, size=0):
        """
        Method that initializes the class and checks
        for good input
        Args:
            self: refers back to the class
            size: default = 0, else defined input
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Method that retrieves the current size for
        the setter to work with
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method that sets the value
        Args:
            self: refers back to the class
            value: value defined
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method that returns the area
        """
        return self.__size ** 2

    def my_print(self):
        """ Method that prints out a square size * size """
        if self.__size == 0:
            print()
            return
        for height in range(self.__size):
            for width in range(self.__size):
                print("#", end="")
            print()
