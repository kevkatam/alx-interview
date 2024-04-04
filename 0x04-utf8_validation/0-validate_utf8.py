#!/usr/bin/python3
"""
validUTF8 module
"""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    for i in data:
        j = bin(i)[2:]
        if len(j) > 8:
            return False

    if len(j) >= 2 and j[:2] != '10':
        return False
    return True
