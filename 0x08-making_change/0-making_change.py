#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount total
    """
    if total < 1:
        return 0
    change = 0
    coins.sort(reverse=True)
    for coin in coins:
        tmp_change = int(total / coin)
        total -= (tmp_change * coin)
        change += tmp_change
        if total == 0:
            return change
    if total != 0:
        return -1
