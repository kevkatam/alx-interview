#!/usr/bin/python3
"""
module that solves the nqueen puzzle
"""


def is_safe(mqueen, nqueen):
    """ function that checks if the queens can or can't kill each other
    Args:
        mqueen: array containing queen position
        nqueen: queen number
    """
    for i in range(nqueen):
        if mqueen[i] == mqueen[nqueen]:
            return False
        if abs(mqueen[i] - mqueen[nqueen]) == abs(i - nqueen):
            return False
    return True


def print_sol(mqueen, nqueen):
    """ function that print's the list with queen's position """
    res = []
    for i in range(nqueen):
        res.append([i, mqueen[i]])
    print(res)


def Queen(mqueen, nqueen):
    """ recursive function performing backtracking algo """
    if nqueen is len(mqueen):
        print_sol(mqueen, nqueen)
        return
    mqueen[nqueen] = -1

    while ((mqueen[nqueen] < len(mqueen) - 1)):
        mqueen[nqueen] += 1
        if is_safe(mqueen, nqueen) is True:
            if nqueen is not len(mqueen):
                Queen(mqueen, nqueen + 1)


def resolve(size):
    """ function that calls the back tracking algo
    Args:
        size: size of the chessboard
    """
    mqueen = [-1 for i in range(size)]
    Queen(mqueen, 0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    resolve(size)
