#!/usr/bin/python3
"""
This module contains two functions.
dec_bin_converter - converts decimal to binary
validUTF8 - validate utf8
"""

from typing import List


def dec_bin_converter(num: int) -> str:
    """
    function converts decimal to binary
    """
    bin_bit = ""

    while num != 0:
        bin_bit += str(num % 2)
        num = int(num / 2)

    # add zeros to string if it is less than 8 bits
    bin_bit_len = len(bin_bit)
    bin_bit += (8 - bin_bit_len)*'0'

    # The following trick reverses a string
    return bin_bit[::-1]


def validUTF8(data: List) -> bool:
    """
    Return True or False if string is valid utf-8 or not
    """
    bin_list = [dec_bin_converter(data[i]) for i in range(0, len(data))]
    bin_list_len = len(bin_list)
    i = 0
    valid = False
    while i < bin_list_len:
        j = 0
        if bin_list[i].startswith('0'):
            j = i + 1
        elif bin_list[i].startswith('110'):
            j = i + 2
            if j <= bin_list_len:
                for k in range(i + 1, j):
                    if not bin_list[k].startswith('10'):
                        valid = False
                        break
            else:
                valid = False
                break
        elif bin_list[i].startswith('1110'):
            j = i + 3
            if j <= bin_list_len:
                for k in range(i + 1, j):
                    if not bin_list[k].startswith('10'):
                        valid = False
                        break
            else:
                valid = False
                break
        elif bin_list[i].startswith('11110'):
            j = i + 4
            if j <= bin_list_len:
                for k in range(i + 1, j):
                    if not bin_list[k].startswith('10'):
                        valid = False
                        break
            else:
                valid = False
                break
        else:
            valid = False
            break
        i = j

    if i == bin_list_len:
        valid = True

    return valid
