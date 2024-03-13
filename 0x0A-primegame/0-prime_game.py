#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def generate_prime_counts(n):
    """
    Generates an array where each index
    represents a number up to n,
    and the value at each index
    represents the count of primes up to that number.
    """
    is_prime = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    is_prime[0] = is_prime[1] = False
    prime_counts = [0] * (n + 1)
    count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            count += 1
        prime_counts[i] = count
    return prime_counts


def is_winner(x, nums):
    """
    Determines the winner of the most rounds of a prime game
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_counts = generate_prime_counts(max_num)

    maria_wins = sum(prime_counts[n] % 2 == 1 for n in nums)

    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
