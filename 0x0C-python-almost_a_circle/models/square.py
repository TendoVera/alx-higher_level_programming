#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Represents a square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square, which will be used as both width and height.
            x (int, optional): The x-coordinate of the top-left corner of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the top-left corner of the square. Defaults to 0.
            id (int, optional): The identifier of the square. Defaults to None.
        """
    super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
