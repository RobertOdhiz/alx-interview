#!/usr/bin/python3
"""
File with minOperations(n) functions
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n == 1 or not isinstance(n, int):
        return 0

    operations = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operations += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operations += 2
        elif clipboard > 0:
            done += clipboard
            operations += 1

    return operations
