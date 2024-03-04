#!/usr/bin/python3
def makeChange(coins, total):
    """The objective is to find the minimum number of coins required
    to make up a given total amount, given a list of coin denominations.
    Args:
        coins : The denominations of coins available.
        total : The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total amount.
            Returns -1 if the total cannot be met by any coins combination.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coins_counter = 0
    idx = 0

    while total > 0 and idx < len(coins):
        if coins[idx] <= total:
            total -= coins[idx]
            coins_counter += 1
        else:
            idx += 1

    if total == 0:
        return coins_counter
    else:
        return -1
