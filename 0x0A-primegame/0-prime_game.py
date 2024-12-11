#!/usr/bin/python3
""" prime numbers, game theory, and algorithm optimization"""


def isWinner(x, nums):
    """
     Generates a list of prime numbers up to and including `n`
     using the Sieve of Eratosthenes.
     Parameters:
        n (int): The upper limit for prime number generation.
     Returns:
        list: A list of integers representing prime numbers up to `n`.
    """
    def prime_num_in_range_n(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return [i for i in range(n + 1) if is_prime[i]]

    def calculate_winner(n):
        prime_num = prime_num_in_range_n(n)
        if len(prime_num) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [calculate_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
