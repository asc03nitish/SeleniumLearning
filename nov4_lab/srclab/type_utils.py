# src/type_utils.py

from typing import Any


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both parameters must be integers.")
    return a + b


def to_int(value: Any) -> int:
    """Try to convert a value to an integer."""
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Cannot convert {value} to int.")


def is_string(value: Any) -> bool:
    """Check if the value is a string."""
    return isinstance(value, str)


class Student:
    """A simple class for testing instance validation."""
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18
