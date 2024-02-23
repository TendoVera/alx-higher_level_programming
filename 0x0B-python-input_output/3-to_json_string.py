#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json

def to_json_string(my_obj):
    """ Convert an object to its JSON representation.
    Return the JSON-formatted string representing the object.
    """
    return json.dumps(my_obj)
