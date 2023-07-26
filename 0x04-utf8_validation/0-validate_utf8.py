#!/usr/bin/python3
"""
This module contains two functions.
dec_bin_converter - converts decimal to binary
validUTF8 - validate utf8
"""

from typing import List, Tuple


def dec_bin_converter(num: int) -> str:
    """
    function converts decimal to binary
    """
    bin_bit = []

    while num != 0:
        bin_bit.append(str(num % 2))
        num = int(num / 2)

    # add zeros to string if it is less than 8 bits
    bin_bit_len = len(bin_bit)

    if bin_bit_len < 8:
        diff = 8 - bin_bit_len
        for i in range(0, diff):
            bin_bit.append('0')

    if bin_bit_len > 8:
        diff = bin_bit_len - 8
        for i in range(0, diff):
            bin_bit.pop()

    bin_bit.reverse()
    return "".join(bin_bit)

def validity(idx: int, bin_list: List, codept: int) -> Tuple:
    """
    validity - Test a codepoint of binary list for validity
    Returns true or false if code point conditions are fulfilled
    """
    code_point = {"0": 1, "110": 2, "1110": 3, "11110": 4}
    valid = True
    j = idx + code_point[codept]

    if codept == "0":
        return (valid, j)

    bin_list_len = len(bin_list)

    if j <= bin_list_len:
        for k in range(idx + 1, j):
            if not bin_list[k].startswith('10'):
                valid = False
                break
    else:
        valid = False
    return (valid, j)


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
            vi = validity(i, bin_list, '0')
            valid = vi[0]
            j = vi[1]
        elif bin_list[i].startswith('110'):
            vi = validity(i, bin_list, '110')
            valid = vi[0]
            if valid == False:
                break
            j = vi[1]
        elif bin_list[i].startswith('1110'):
            vi = validity(i, bin_list, '1110')
            valid = vi[0]
            if valid == False:
                break
            j = vi[1]
        elif bin_list[i].startswith('11110'):
            vi = validity(i, bin_list, '11110')
            valid = vi[0]
            if valid == False:
                break
            j = vi[1]
        else:
            valid = False
            break
        i = j

    if i == bin_list_len:
        valid = True

    return valid
