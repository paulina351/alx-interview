#!/usr/bin/python3
"""
Minimum Operations
"""


def primeFactor(z):
    """Getting the prime
    """
    divide = 2
    array = list()
    while (divide <= z):
        if z % divide == 0:
            array.append(divide)
            z /= divide
        else:
            divide += 1

    return array


def minOperations(n):
    """A method that calculates the fewest number of operations
        needed to result in exactly n H characters in the file.
    """
    minimun = 0
    fact = [z for z in primeFactor(n)]
    appearances = {item: fact.count(item) for item in fact}
    for a, b in appearances.items():
        minimum += a * b
    return minimum
