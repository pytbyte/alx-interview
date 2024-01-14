#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Generates Pascal's triangle up to a specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of lists: Pascal's triangle represented as a list of lists.
    '''
    triangle = []

    if not isinstance(n, int) or n <= 0:
        return triangle

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 0 and 0 < j < i:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(row)

    return triangle
