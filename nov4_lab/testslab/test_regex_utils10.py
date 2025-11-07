import re
import pytest

# -----------------------------
# Utility functions (regex-based)
# -----------------------------

def is_valid_email(email: str) -> bool:
    """Validate email address format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    """Validate international or local phone number formats."""
    pattern = r'^(\+\d{1,3}[- ]?)?\d{10}$'
    return bool(re.match(pattern, phone))


def is_strong_password(password: str) -> bool:
    """
    Validate password strength.
    Must contain:
      - At least 8 characters
      - One uppercase letter
      - One lowercase letter
      - One number
      - One special character
    """
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$'
    return bool(re.match(pattern, password))


def is_valid_url(url: str) -> bool:
    """Basic URL validation."""
    pattern = r'^(https?:\/\/)?([\w\-]+\.)+[a-z]{2,6}(:\d+)?(\/[^\s]*)?$'
    return bool(re.match(pattern, url))


# -----------------------------
# Pytest test cases
# -----------------------------

# Email tests
@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("user.name@domain.co.in", True),
    ("invalid-email", False),
    ("user@.com", False),
    ("@domain.com", False),
])
def test_email_validation(email, expected):
    assert is_valid_email(email) == expected


# Phone number tests
@pytest.mark.parametrize("phone,expected", [
    ("9876543210", True),
    ("+919876543210", True),
    ("09123456789", False),  # too many digits
    ("12345", False),
    ("+1-1234567890", True),
])
def test_phone_validation(phone, expected):
    assert is_valid_phone(phone) == expected


# Password strength tests
@pytest.mark.parametrize("password,expected", [
    ("Strong@123", True),
    ("weakpass", False),
    ("N0SpecialChar", False),
    ("@Short1", False),
    ("Valid#Pass9", True),
])
def test_password_strength(password, expected):
    assert is_strong_password(password) == expected


# URL validation tests
@pytest.mark.parametrize("url,expected", [
    ("https://www.google.com", True),
    ("http://example.org/path", True),
    ("ftp://example.com", False),
    ("invalid-url", False),
    ("https://sub.domain.co.in:8080/test", True),
])
def test_url_validation(url, expected):
    assert is_valid_url(url) == expected
