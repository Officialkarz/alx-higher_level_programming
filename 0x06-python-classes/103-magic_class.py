#!/usr/bin/python3
""" ByteCode -> Python #5
"""


import math


class MagicClass:
    """ Python bytecode.
    """

    def __init__(self, radius=0):
        """ Stores the properties of a circumference
        Args:
            radius: the radus value
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Calculates the area of the circumference
        Returns: the area of the circumference
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """ Calculates the perimeter of a circumference
        Returns: the circumference
        """
        return (2 * math.pi * self.__radius)
