#!/usr/bin/python3
"""
module containing solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """ returns true or false depending if all boxes can be opened """
    unlocked = {0}

    keys = boxes[0]

    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
