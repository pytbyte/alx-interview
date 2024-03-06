#!/usr/bin/python3
"""Module for computing the perimeter of an island."""

def island_perimeter(grid):
    """
    Computes the perimeter of an island represented by a grid.

    Args:
        grid (list of list of int): Represents the island, where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    if not isinstance(grid, list):
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if grid[row_index][col_index] == 1:
                edges = [
                    (row_index == 0 or grid[row_index - 1][col_index] == 0),
                    (col_index == num_cols - 1 or grid[row_index][col_index + 1] == 0),
                    (row_index == num_rows - 1 or grid[row_index + 1][col_index] == 0),
                    (col_index == 0 or grid[row_index][col_index - 1] == 0)
                ]
                perimeter += sum(edges)

    return perimeter
