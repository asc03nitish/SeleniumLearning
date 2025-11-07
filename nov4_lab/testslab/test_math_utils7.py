# Experiments/tests/test_math_utils.py
import math
import pytest
from nov4_lab.srclab.math_utils import (
    fibonacci, is_prime,
    calculate_mean, calculate_median,
    area_of_circle, area_of_triangle
)

# --- Fibonacci Tests ---
def test_fibonacci_basic():
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_zero():
    assert fibonacci(0) == []

def test_fibonacci_one():
    assert fibonacci(1) == [0]

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-3)


# --- Prime Tests ---
def test_prime_numbers():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7919)

def test_non_prime_numbers():
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(9)
    assert not is_prime(7920)


# --- Statistics Tests ---
def test_mean_and_median_basic():
    assert calculate_mean([1, 2, 3, 4, 5]) == 3
    assert calculate_median([1, 3, 5]) == 3
    assert calculate_median([1, 2, 3, 4]) == 2.5

def test_empty_statistics():
    with pytest.raises(ValueError):
        calculate_mean([])
    with pytest.raises(ValueError):
        calculate_median([])


# --- Geometry Tests ---
def test_area_of_circle():
    assert math.isclose(area_of_circle(1), math.pi, rel_tol=1e-9)
    assert area_of_circle(0) == 0
    with pytest.raises(ValueError):
        area_of_circle(-2)

def test_area_of_triangle():
    assert area_of_triangle(10, 5) == 25.0
    with pytest.raises(ValueError):
        area_of_triangle(-10, 5)
