#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """
    Given that only 2 operations are allowed,
    The minimum operation to get n characters
    in a text editor is the operations of minimum operation
    to get all the prime factors of n.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    i = 0
    prime_number_determinants = [2, 3, 5, 7]
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

    return operations
