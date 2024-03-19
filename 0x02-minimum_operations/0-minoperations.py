#!/usr/bin/python3
"""
module containing function that is solution to minimum operations problem
"""


def minOperations(n):
    """ function that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n == 1:
        return 0
    arr = []
    while n % 2 == 0:
        arr.append(2)
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            arr.append(i)
            n //= i
    if n > 2:
        arr.append(n)
    return sum(arr)
