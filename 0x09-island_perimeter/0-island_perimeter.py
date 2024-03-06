def calculate_island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of lists of int): Represents the island, where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += calculate_cell_perimeter(grid, i, j)

    return perimeter

def calculate_cell_perimeter(grid, i, j):
    """
    Calculate the perimeter contribution of a single cell.

    Args:
        grid (list of lists of int): Represents the island.
        i (int): Row index of the cell.
        j (int): Column index of the cell.

    Returns:
        int: The perimeter contribution of the cell.
    """
    perimeter_contribution = 0

    # Check the adjacent cells
    if i == 0 or grid[i - 1][j] == 0:
        perimeter_contribution += 1
    if i == len(grid) - 1 or grid[i + 1][j] == 0:
        perimeter_contribution += 1
    if j == 0 or grid[i][j - 1] == 0:
        perimeter_contribution += 1
    if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
        perimeter_contribution += 1

    return perimeter_contribution

# Example usage:
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(calculate_island_perimeter(grid))  
