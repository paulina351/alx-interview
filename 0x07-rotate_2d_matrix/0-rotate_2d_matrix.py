#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    n = len(matrix)
    for a in range(int(n / 2)):
        d = (n - a - 1)
        for b in range(a, d):
            c = (n - 1 - b)
            tmp = matrix[a][b]
            matrix[a][b] = matrix[c][a]

            matrix[c][a] = matrix[d][c]

            matrix[d][c] = matrix[b][d]

            matrix[b][d] = tmp
