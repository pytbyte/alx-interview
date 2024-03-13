#!/usr/bin/python3

def is_prime(num):
    """
    Check if a number is prime.

    Args:
        num (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): The number of rounds to play.
        nums (list): A list of integers representing the values of 'n' for each round.

    Returns:
        str or None: The name of the player that won the most rounds. Returns 'Maria',
                     'Ben', or None if the winner cannot be determined.
    """
    if not nums or x <= 0:
        return None

    wins_maria, wins_ben = 0, 0

    for n in nums:
        primes_left = [i for i in range(1, n + 1) if is_prime(i)]

        current_player = "Maria"
        while primes_left:
            move = min(primes_left)
            primes_left = [num for num in primes_left if num % move != 0]

            if not primes_left:
                break

            current_player = "Ben" if current_player == "Maria" else "Maria"

        if current_player == "Maria":
            wins_maria += 1
        else:
            wins_ben += 1

    return "Maria" if wins_maria > wins_ben else "Ben" if wins_ben > wins_maria else None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
