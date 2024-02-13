#!/usr/bin/python3
"""Defines an integer addition function."""
def add_integer(a, b=98):
    """Check if a and b are integers or floats
    Raises:
        TypeError: If either of a or b is a non-integer and non-float
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    """Return the addition of a and b"""
    return a + b
