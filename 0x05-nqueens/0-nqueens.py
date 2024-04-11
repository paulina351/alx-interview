#!/usr/bin/python3
"""N queens"""

import sys


def birth_board(board, n):
    """a program that solves the N queens problem.
    """
    a = []

    for b in range(n):
        for c in range(n):
            if c == board[b]:
                a.append([b, c])
    print(a)


def unsafe_position(board, b, c, d):
    """The N queens puzzle is the challenge of
        placing N non-attacking queens on an N×N chessboard.
    """
    return board[b] in (c, c - b + d, b - d + c)


def position_insitu(board, row, n):
    """a program that solves the N queens problem.
    """
    if row == n:
        birth_board(board, n)
    else:
        for c in range(n):
            allowed = True
            for b in range(row):
                if unsafe_position(board, b, c, row):
                    allowed = False
            if allowed:
                board[row] = c
                position_insitu(board, row + 1, n)


def build_board(size):
    """creating a new board"""
    return [0 * size for b in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = build_board(int(n))
row = 0
position_insitu(board, row, int(n))
