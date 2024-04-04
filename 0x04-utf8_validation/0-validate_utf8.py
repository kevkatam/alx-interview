#!/usr/bin/python3
"""
validUTF8 module
"""


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    for i in data:
        if i > 255:
            return False
    return True
