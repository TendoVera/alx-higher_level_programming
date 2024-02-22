#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        print(f"Error writing to file: {e}")
        return 0
