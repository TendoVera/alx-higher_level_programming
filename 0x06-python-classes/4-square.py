#!/usr/bin/python3
"""Represent a square."""
class Square:
    """Class defines a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size
    @property
    def size(self):
        """
        Setter method for retrieving the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of square."""
        return (self.__size * self.__size)
