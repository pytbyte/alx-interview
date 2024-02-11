#!/usr/bin/python3
"""N queens solution finder module.
"""

import sys

solutions = []
n = 0
pos = None


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    return pos0[0] == pos1[0] or pos0[1] == pos1[1] or abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """Checks if a group exists in the list of solutions.

    Args:
        group (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions, n
    for solution in solutions:
        if all(position in solution for position in group):
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the N queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions, n
    if row == n:
        temp_group = group.copy()
        if not group_exists(temp_group):
            solutions.append(temp_group)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    row = 0
    group = []
    build_solution(row, group)


if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)
