import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_value_error():
    with pytest.raises(ValueError):
        int("not_a_number")


def test_specific_exception_message():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")


# Testing custom exceptions
def test_calculator_division_by_zero():
    from nov4_class.src.calculator import Calculator

    calc = Calculator()

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_factorial_negative_number():
    from nov4_class.src.calculator import Calculator

    calc = Calculator()

    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        calc.factorial(-5)
