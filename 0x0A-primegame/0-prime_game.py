#!/usr/bin/python3
"""
module containing solution to prime game
"""


def prime_numbers(n):
    """function that returns list of prime numbers """
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p]):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    primelist = []
    for p in range(2, n + 1):
        if prime[p]:
            primelist.append(p)
    return primelist


def isWinner(x, nums):
    """function that determines the winner in a prime game """
    if x is None or nums is None:
        return None
    if x == 0 or nums == []:
        return None

    maria = 0
    ben = 0

    for i in range(x):
        primes = prime_numbers(nums[i])
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return 'Ben'
    else:
        return 'Maria'
    return None
