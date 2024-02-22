#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """Print the contents of a UTF text file to stdout.
    Args:
        filename (str): The name of the text file to be read.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print("File not found.")
