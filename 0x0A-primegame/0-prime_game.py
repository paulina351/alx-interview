#!/usr/bin/python3
"""
0. Prime Game
"""


def isWinner(x, nums):
    """Maria and Ben are playing a game. Given a set of
        consecutive integers starting from 1 up to and including
        n, they take turns choosing a prime number from the set
        and removing that number and its multiples from the set.
        The player that cannot make a move loses the game.
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    game = [True for _ in range(max(n + 1, 2))]
    for a in range(2, int(pow(n, 0.5)) + 1):
        if not game[a]:
            continue
        for b in range(a * a, n + 1, a):
            game[b] = False
    game[0] = game[1] = False
    d = 0
    for a in range(len(game)):
        if game[a]:
            d += 1
        game[a] = d
    maria1 = 0
    for n in nums:
        maria1 += game[n] % 2 == 1
    if maria1 * 2 == len(nums):
        return None
    if maria1 * 2 > len(nums):
        return "Maria"
    return "Ben"
