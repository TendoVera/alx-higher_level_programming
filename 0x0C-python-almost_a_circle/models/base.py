#!/usr/bin/python3
"""Module for the base"""

class Base:
    """The class represents class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object.

        Args:
            id (int): The id to assign to the object. If None, a new id will be on __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
