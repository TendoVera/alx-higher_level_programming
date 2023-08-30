#!/usr/bin/python3
"""defining a square"""
class Square:
  """class named Square"""
  def __init__(self, size=0):
    """the area of square is calculated.
    Args:
    size: the value of the area.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
  def area(self):
    return (self.__size * self.__size)
