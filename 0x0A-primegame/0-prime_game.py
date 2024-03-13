#!/usr/bin/python3
""" Module for solving prime game question """


def isWinner(x_rounds, nums):
    """
    Determine the winner of the prime game.

    Args:
        x_rounds (int): The number of rounds to play.
        nums (list): A list of integers
        representing the values of 'n' for each round.

    Returns:
        str or None: The name of the player that
        won the most rounds. Returns 'Maria',
        'Ben', or None if the winner cannot be determined.
    """
    if not nums or x_rounds < 1:
        return None
    max_num = max(nums)

    prime_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not prime_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            prime_filter[j] = False
    prime_filter[0] = prime_filter[1] = False
    prime_count = 0
    for i in range(len(prime_filter)):
        if prime_filter[i]:
            prime_count += 1
        prime_filter[i] = prime_count
    player1_wins = 0
    for x_value in nums:
        player1_wins += prime_filter[x_value] % 2 == 1
    if player1_wins * 2 == len(nums):
        return None
    if player1_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
