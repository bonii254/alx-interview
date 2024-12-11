# Prime Number Game

## Overview

This project implements a game that involves prime numbers, game theory, and algorithm optimization. The primary function `isWinner` determines the winner between two players, Maria and Ben, based on a series of rounds where they take turns selecting prime numbers from a given range.

## Files

- **`0-prime_game.py`**: Contains the core logic for the prime number game.
- **`main_0.py`**: Example script to test the `isWinner` function.

## Function Descriptions

### `isWinner(x, nums)`

Determines the winner of a series of rounds based on prime numbers.

#### Parameters

- **`x`** *(int)*: Number of rounds to play.
- **`nums`** *(list of int)*: A list where each element represents the upper limit `n` for a given round.

#### Returns

- **`str`**: The winner's name ("Maria" or "Ben") or `None` if it's a draw.

#### Game Rules

1. In each round, players take turns picking prime numbers from a range `[1, n]`.
2. Once a prime number is chosen, all its multiples are removed from the list.
3. The player who cannot make a move loses.
4. Maria always goes first.

---

### Internal Functions

#### `prime_num_in_range_n(n)`

Generates a list of prime numbers up to and including `n` using the Sieve of Eratosthenes.

- **Parameters**:  
  `n` *(int)*: The upper limit for prime number generation.

  - **Returns**:  
    `list` of prime numbers up to `n`.

#### `calculate_winner(n)`

Determines the winner for a single round based on the number of prime numbers up to `n`.

- **Parameters**:  
  `n` *(int)*: The upper limit for prime number generation in this round.

  - **Returns**:  
    `"Maria"` if the number of primes is odd, `"Ben"` if even.

    ---

## Example Usage

Create a script `main_0.py` to test the game:

```python
#!/usr/bin/python3
from 0-prime_game import isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
