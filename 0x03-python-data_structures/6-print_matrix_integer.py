#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in matrix:
        for i in n:
            print("{}".format(i), end=" " if i != n[-1] else "")
