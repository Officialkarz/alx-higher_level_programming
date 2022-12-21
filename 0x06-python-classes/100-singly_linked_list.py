#!/usr/bin/python3
""" A module that operates like single linked list.
"""


class Node:
    """ A class that defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """ Built in method for intiallization.
        Args:
            data (int): integer data to be added to node
            next_node: points to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Returns or retrive value for setted
        Returns: the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the data's value.
        Args:
            value (int): values to be setted.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Method that retrive the next_node.
        Returns: the next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the next_node's value.
        Args:
            next_node (int): next_node to be setted.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ A class that defines a singly linked list
    """
    def __str__(self):
        """ Built in str method
        Returns: the output
        """
        output = ""
        point = self.__head

        while point is not None:
            output += str(point.data)
            if point.next_node is not None:
                output += "\n"
            point = point.next_node

        return output

    def __init__(self):
        """ Builtin method for intallization
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Sorts the value
        Args:
           value (int): integer value
        """
        point = self.__head

        while point is not None:
            if point.data > value:
                break
            ptr_prev = point
            point = point.next_node

        newNode = Node(value, point)
        if point == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
