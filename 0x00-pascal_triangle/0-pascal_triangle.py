#!/usr/bin/python3
"""
  This module contains the solution to the pascal triangle imbroglio.
  The solution is recursive
"""


def latest_list(list_array=[]):
    """
      This function adds every 2 elements of the array given as para
      meter to produce a new array.
      list_array - is an array parameter
    """
    new_list = [1, 1]
    length = len(list_array)

    if list_array == [] or list_array is None:
        return [1]
    if list_array == [1]:
        return new_list
    for i in range(1, length):
        new_list.insert(i, list_array[i] + list_array[i - 1])

    return new_list


def pascal_triangle(n):
    """
      This function computes the pascal triangle recursively
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    big_list = []
    big_list = pascal_triangle(n - 1)
    length = len(big_list) - 1
    big_list.append(latest_list(big_list[length]))

    return big_list
