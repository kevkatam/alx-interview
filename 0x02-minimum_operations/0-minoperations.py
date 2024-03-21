#!/usr/bin/python3
"""
module containing function that is solution to minimum operations problem
"""


def minOperations(n):
    """ function that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    op = 0
    clip = 2

    while n > 1:
        while n % clip == 0:
            op += clip
            n /= clip
        clip += 1
    return op
