#!/usr/bin/python3
'''Minimum operations interview.
'''


def min_operations_to_generate(n):
    '''
    Computes the fewest number of operations needed to generate
    exactly n H characters using Copy All and Paste operations.
    '''
    if not isinstance(n, int) or n <= 0:
        # Invalid input, return 0 as it's impossible to achieve.
        return 0

    total_operations = 0
    clipboard_content = 0
    characters_generated = 1

    # Perform operations until the desired number of characters is achieved.
    while characters_generated < n:
        if clipboard_content == 0:
            # If clipboard is empty, perform an initial Copy All and Paste.
            clipboard_content = characters_generated
            characters_generated += clipboard_content
            total_operations += 2
        elif (n - characters_generated) % characters_generated == 0:
            # If the remaining characters can be evenly divided,
            # perform another Copy All and Paste.
            clipboard_content = characters_generated
            characters_generated += clipboard_content
            total_operations += 2
        elif clipboard_content > 0:
            # Perform a Paste operation.
            characters_generated += clipboard_content
            total_operations += 1

    return total_operations
