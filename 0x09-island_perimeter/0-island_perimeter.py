#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
    grid (list of list of int): A 2D grid representing the island, where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0

    # Helper function to check if a cell is within the bounds of the grid
    def is_valid_cell(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    # Helper function to calculate perimeter of a cell
    def calculate_cell_perimeter(x, y):
        count = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not is_valid_cell(nx, ny) or grid[nx][ny] == 0:
                count += 1
        return count

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += calculate_cell_perimeter(i, j)

    return perimeter

# Test the function
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(island_perimeter(grid))
