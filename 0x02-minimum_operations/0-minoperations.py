#!/usr/bin/python3
"""
module containing function that is solution to minimum operations problem
"""


def minOperations(n):
    """ function that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    arr = [1, 2]
    if n % 3 == 0:
        for i in range(3, n+1, 3):
            arr.append(i)
    elif n % 2 == 0:
        for i in range(3, n+1, 2):
            arr.append(i)
    else:
        for i in range(3, n+1, 1):
            arr.append(i)
    return len(arr) + 1
