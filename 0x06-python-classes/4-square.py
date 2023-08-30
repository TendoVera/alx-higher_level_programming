#!/usr/bin/python3
"""defining a class"""
class Square:
  def __init__(self, size=0):
    """new square.
    Args:
    size (int): size value of new sqaure.
    """
    self.__size = size
  @property
  def size(self):
      return (self.__size)

  @size.setter
  def size(self, value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value
    """setter makes sure values are >= 0"""
  def area(self):
      return (self.__size * self.__size)
