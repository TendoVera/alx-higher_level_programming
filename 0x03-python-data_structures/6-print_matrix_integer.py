#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for number in matrix:
        print(' '.join('{:d}'.format(j)for j in number))
