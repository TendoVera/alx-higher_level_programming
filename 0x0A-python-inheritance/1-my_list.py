#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """MyList class inherits from the built-in list class and adds functionality.
    Methods:
        print_sorted(): Prints the elements of the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
