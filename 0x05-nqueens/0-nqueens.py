#!/usr/bin/python3
"""
N queens solution finder module.
"""
import sys


def print_solution(solution):
    """Prints the N-Queens solution."""
    for pos in solution:
        print(pos)
    print()


def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    """Recursively solves the N-Queens problem."""
    if row == n:
        print_solution([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """Wrapper function to initialize the board and start solving."""
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
