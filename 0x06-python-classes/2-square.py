#!/usr/bin/python3
""" Square """


class Square:
    """Square Initialization"""
    __size = None

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
