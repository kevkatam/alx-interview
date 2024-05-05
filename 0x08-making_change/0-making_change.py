#!/usr/bin/python3
"""
module containing making changer answer
"""


def makeChange(coins, total):
    """determine the fewest number of coins needed to meet a given amount
    """

    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1

    try:
        coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    count = 0
    for i in coins:
        if total % i == 0:
            count += int(total / i)
            return count
        if total - i >= 0:
            if int(total / i) > 1:
                count += int(total / i)
                total = total % i
            else:
                count += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return count
