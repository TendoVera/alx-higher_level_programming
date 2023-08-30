#!/usr/bin/python3
"""define a sqaure"""
class Square:
  def __init__(self, size=0):
    """to check size of sqaure.
    Args:
    size: the value of size.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
