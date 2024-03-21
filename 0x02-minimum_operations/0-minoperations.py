#!/usr/bin/python3
"""
module containing function that is solution to minimum operations problem
"""


def minOperations(n):
    """ function that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    op = 0
    add = 1
    car = 0

    while add < n:
        if n % add == 0:
            car = add
            add *= 2
            op += 1
        else:
            add += car
        op += 1
    return op
