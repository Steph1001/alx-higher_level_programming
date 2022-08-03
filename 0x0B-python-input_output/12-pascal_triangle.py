#!/usr/bin/python3
"""Module 14-pascal_triangle.
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.

    Args:
        - n: size of the triangle (rows)

    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    list_p = [[0 for x in range(i + 1)] for i in range(n)]
    list_p[0] = [1]

    for i in range(1, n):
        list_p[i][0] = 1
        for j in range(1, i + 1):
            if j < len(list_p[i - 1]):
                list_p[i][j] = list_p[i - 1][j - 1] + list_p[i - 1][j]
            else:
                list_p[i][j] = list_p[i - 1][0]
    return list_p
