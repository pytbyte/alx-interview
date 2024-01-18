#!/usr/bin/python3
'''Minimum operations coding challenge.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters using Copy All and Paste operations.
    '''
    if not isinstance(n, int) or n <= 0:
        return 0

    operations_count = 0
    clipboard = 0
    resulting_characters = 1

    # Perform operations until the desired number of characters is achieved.
    # works by splitting into 2 and checking further
    while resulting_characters < n:
        if clipboard == 0:
            clipboard = resulting_characters
            resulting_characters += clipboard
            operations_count += 2
        elif (n - resulting_characters) % resulting_characters == 0:
            clipboard = resulting_characters
            resulting_characters += clipboard
            operations_count += 2
        elif clipboard > 0:
            
            resulting_characters += clipboard
            operations_count += 1

    return operations_count
