#!/usr/bin/python3
"""
   Minimum Operations
   Returns minimimum number of operations
"""


def minOperations(n):
    """
    Given that only 2 operations are allowed,
    The minimum operation to get n characters
    in a text editor is the operations of minimum operation
    to get all the prime factors of n.
    """
    if n <= 1:
        return 0
    if not isinstance(n, int):
        return 0

    operations = 0
    i = 0
    prime_number_determinants =
    [
        2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97,
        101, 103, 107, 109, 113, 127, 131,
        137, 139, 149, 151, 157, 163, 167,
        173, 179, 181, 191, 193, 197, 199
    ]

    size = len(prime_number_determinants)

    while i < size:
        pnd = prime_number_determinants[i]

        if n % pnd == 0:
            operations += pnd
            n = n / pnd
        else:
            i += 1
        if i == size:
            if n > 1:
                operations += n

    return int(operations)
