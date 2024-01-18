#!/usr/bin/python3
'''Minimum operations head knock.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters using Copy All and Paste operations.
    '''
    if not isinstance(n, int) or n <= 0:
        return 0

    operations_count = 0
    buffer = 0
    resulting_characters = 1

    # Perform operations until the desired number of characters is achieved.
    # works by splitting into 2 and checking further
    while resulting_characters < n:
        if buffer == 0:
            buffer = resulting_characters
            resulting_characters += buffer
            operations_count += 2
        elif (n - resulting_characters) % resulting_characters == 0:
            buffer = resulting_characters
            resulting_characters += buffer
            operations_count += 2
        elif buffer > 0:
            resulting_characters += buffer
            operations_count += 1
    return operations_count
