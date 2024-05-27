#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """A method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    numb, div, numOfOprationss = n, 2, 0

    while numb > 1:
        if numb % div == 0:
            numb = numb / div
            numOfOprationss = numOfOprationss + div
        else:
            div += 1
    return numOfOprationss
