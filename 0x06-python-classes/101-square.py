#!/usr/bin/python3
""" This module does the calculation for area.
"""


class Square:
    """ This class do calculation for square.
    """
    def __str__(self):
        display = ""

        if self.size == 0:
            return display

        for i in range(self.position[1]):
            display += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                display += " "
            for j in range(self.size):
                display += "#"
            if i is not (self.size - 1):
                display += "\n"

        return display

    def __init__(self, size=0, position=(0, 0)):
        """ This is the intialization builtin fuction.
        Args:
            size (int): the size of squares
            position (int): the position of blank
        Raises:
            ValueError: raises the value error exception
            TypeError: raises the type error in case -ve number
        """
        self.__size = size
        self.position = position
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """ This is the function that retrieve size.
        Returns: the retrived size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is the function that set size.
        Args:
            value (int): the size of squares
        Raises:
            ValueError: raises the value error exception
            TypeError: raises the type error in case -ve number
        """
        self.__size = value
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ Method that retrives the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Prints the square with hash tag.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
