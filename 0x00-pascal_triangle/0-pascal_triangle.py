#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """
    Defines a function that returns a list of integers representing
    Pascal's triangle of n:
    Returns an empty list if n <= 0
    Assuming n will be always an integer
    """
    tri = []
    if not isinstance(n, int) or n <= 0:
        return tri
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(tri[i - 1][j - 1] + tri[i - 1][j])
        tri.append(line)
    return tri
