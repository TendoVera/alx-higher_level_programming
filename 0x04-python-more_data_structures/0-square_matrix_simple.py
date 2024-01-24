#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = [[0 for _ in row] for row in matrix]
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            result_matrix[a][b] = matrix[a][b] ** 2

    return result_matrix
