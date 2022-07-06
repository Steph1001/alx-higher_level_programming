#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        return list(map(lambda x: [i*i for i in x], matrix.copy()))
