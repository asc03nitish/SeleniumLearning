# Experiments/src/math_utils.py

import math
from statistics import mean, median

# --- Fibonacci Sequence ---
def fibonacci(n):
    if n < 0:
        raise ValueError("Input cannot be negative")
    seq = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq


# --- Prime Number Check ---
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


# --- Statistics ---
def calculate_mean(numbers):
    if not numbers:
        raise ValueError("Empty list provided")
    return mean(numbers)

def calculate_median(numbers):
    if not numbers:
        raise ValueError("Empty list provided")
    return median(numbers)


# --- Geometry ---
def area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def area_of_triangle(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height
