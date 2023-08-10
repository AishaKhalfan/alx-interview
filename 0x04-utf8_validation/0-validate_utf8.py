#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data
    Return:
        True - if data is a valid UTF-8 encoding,
        False -  if data is not a valid UTF-8 encoding,
    """
    successive_10 = 0
    for b in data:
        b = bin(b).replace('0b', '').rjust(8, '0')
        if successive_10 != 0:
            successive_10 -= 1
            if not b.startswith('10'):
                return False
        elif b[0] == '1':
                successive_10 = len(b.split('0')[0]) - 1
    return True
