#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s triangle of n:
"""
def pascal_triangle(n):
    """pascal triangle
    returns an empty list if n <= 0
    n will always be an integer.
    """

    n = int(input("Enter the number of rows for Pascal's Triangle: "))
    
    triangle = []

    for x in range(n):
        row = []
        for y in range(x + y):
            if y == 0 or y == x:
                row.append(1)
            else:
                previous_row = triangle[x - 1]
                row.append(previous_row[y - 1] + previous_row[y])
    triangle.append(row)

    for row in triangle:
        print(" ".join(map(str, row)).center(n * 3))