#!/usr/bin/python3
"""defininf the class"""
class Square:
  """square defines the class"""
  def __init__(self, size=0):
    """creating a square.
    Args:
    size (int): size of the square.
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

  def area(self):
      return (self.__size ** 2)
  def my_print(self):
    for i in range(0, self.__size):
        print('#' * self.__size)
    if self.__size == 0:
        print("")
