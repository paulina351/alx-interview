#!/usr/bin/python3
"""
Returns a list of lists of integers
representing the Pascal’s triangle of n:
"""
def pascal_triangle(n):
    """pascal triangle
    returns an empty list if n <= 0
    n will always be an integer.
    """

    if type(n) is not int and n < 0:
        return ([])
    row = []
    for a in range(n):
        row.append([])
        row[a].append(1)
        if (a > 0):
            for b in range(1, a):
                row[a].append(row[a - 1][b - 1] + row[a - 1][b])
            row[a].append(1)


    return (row)
