#!/usr/bin/python3
""" This module does the calculation for area.
"""


class Square:
    """ This class do calculation for square. """
    def __init__(self, size=0):
        """ This is the intialization builtin fuction.
        Args:
            size (int): the size of squares
        """
        self.__size = size
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
