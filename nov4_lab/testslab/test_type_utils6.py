# tests/test_type_utils.py

import pytest
from nov4_lab.srclab.type_utils import add_numbers, to_int, is_string, Student

# --- Function return type validation ---
def test_add_numbers_return_type():
    result = add_numbers(5, 10)
    assert isinstance(result, int)
    assert result == 15

def test_add_numbers_type_error():
    with pytest.raises(TypeError):
        add_numbers("5", 10)


# --- Parameter type enforcement ---
@pytest.mark.parametrize("a,b", [
    (5, "10"),
    (3.5, 2),
    ("a", "b")
])
def test_add_numbers_invalid_types(a, b):
    with pytest.raises(TypeError):
        add_numbers(a, b)


# --- Type conversion tests ---
@pytest.mark.parametrize("value,expected", [
    ("123", 123),
    (45.6, 45),
    (True, 1),
])
def test_to_int_valid(value, expected):
    assert to_int(value) == expected

@pytest.mark.parametrize("value", [
    ("abc"), (None), ("12.3a")
])
def test_to_int_invalid(value):
    with pytest.raises(ValueError):
        to_int(value)


# --- Type checking utility ---
@pytest.mark.parametrize("value,expected", [
    ("hello", True),
    (123, False),
    (None, False),
    (b"bytes", False),
])
def test_is_string(value, expected):
    assert is_string(value) == expected


# --- Custom class instance validation ---
def test_student_instance_creation():
    student = Student("Alice", 20)
    assert isinstance(student, Student)
    assert student.name == "Alice"
    assert student.age == 20
    assert student.is_adult() is True

def test_student_invalid_name_type():
    with pytest.raises(TypeError):
        Student(123, 20)

def test_student_invalid_age_type():
    with pytest.raises(TypeError):
        Student("Alice", "twenty")


# --- Custom class behavior ---
def test_student_adult_check():
    minor = Student("Bob", 15)
    adult = Student("Carol", 22)
    assert minor.is_adult() is False
    assert adult.is_adult() is True
