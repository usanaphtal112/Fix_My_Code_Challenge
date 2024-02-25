#!/usr/bin/python3
"""FizzBuzz

This script implements the FizzBuzz game logic. It prints numbers from 1 to the
given number, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz",
and multiples of both 3 and 5 with "FizzBuzz".

Usage:
    ./0-fizzbuzz.py <number>

Example:
    ./0-fizzbuzz.py 89

Args:
    <number>: The upper limit of numbers to print, inclusive.

"""
import sys


def fizzbuzz(n):
    """Prints FizzBuzz sequence up to a given number.

    Args:
        n (int): The upper limit of numbers to print, inclusive.

    Returns:
        None

    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
