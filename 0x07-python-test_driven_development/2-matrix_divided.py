#!/usr/bin/python3
"""Defines a matrix division function."""
def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """Raise:
    TypeError: If div is not an int or float.
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    """Raise:
    ZeroDivisionError: If div is 0.
    """

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    """Return: new matrix."""
    return new_matrix
