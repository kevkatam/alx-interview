#!/usr/bin/python3
"""
validUTF8 module
"""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """

    valid = 0
    for i in data:
        if i <= 191 and i >= 128:
            if not valid:
                return False
            valid -= 1
        else:
            if valid:
                return False
            if i <= 127:
                continue
            elif i <= 223:
                valid = 1
            elif i <= 239:
                valid = 2
            elif i <= 247:
                valid = 3
            else:
                return False
    return valid == 0
