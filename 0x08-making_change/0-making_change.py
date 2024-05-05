#!/usr/bin/python3
"""
module containing making changer answer
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount
       total
    """
    n = len(coins)
    if total <= 0:
        return 0

    dp = [total + 1 for i in range(total + 1)]

    dp[0] = 0
    for i in range(1, total + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[total] > total:
        return -1
    return dp[total]
