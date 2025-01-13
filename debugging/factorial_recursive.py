#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given number using recursion.

    Parameters:
    n (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number 'n'. 
          If n is 0, returns 1 (since 0! = 1).
    """
    if n == 0:
        return 1  # Base case: 0! is 1
    else:
        return n * factorial(n - 1)  # Recursive call: n! = n * (n-1)!

# Read the input number from command line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))  # Convert the first argument to an integer and pass it to factorial
print(f)  # Print the result of the factorial calculation

