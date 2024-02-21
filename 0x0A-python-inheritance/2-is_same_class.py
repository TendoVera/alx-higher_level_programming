#!/usr/bin/python3
"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compar to.
    Returns:
        True f obj is an instance of a_class.
        False if Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
