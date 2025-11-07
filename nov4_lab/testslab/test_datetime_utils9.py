# Experiments/tests/test_datetime_utils.py
import pytest
from datetime import datetime, date
from zoneinfo import ZoneInfo
from nov4_lab.srclab.datetime_utils import (
    days_between, convert_timezone,
    format_date, calculate_age
)


# --- Date Comparisons & Differences ---
def test_days_between_same_day():
    d = date(2025, 11, 4)
    assert days_between(d, d) == 0

def test_days_between_different_days():
    d1 = date(2025, 11, 1)
    d2 = date(2025, 11, 4)
    assert days_between(d1, d2) == 3


# --- Timezone Conversions ---
def test_timezone_conversion_utc_to_ist():
    naive_dt = datetime(2025, 11, 4, 12, 0, 0)
    converted = convert_timezone(naive_dt, "UTC", "Asia/Kolkata")

    assert converted.tzinfo == ZoneInfo("Asia/Kolkata")
    # UTC → IST (+5:30)
    assert converted.hour == 17 and converted.minute == 30

def test_timezone_conversion_ist_to_utc():
    dt = datetime(2025, 11, 4, 17, 30, 0)
    converted = convert_timezone(dt, "Asia/Kolkata", "UTC")

    assert converted.tzinfo == ZoneInfo("UTC")
    # IST → UTC (-5:30)
    assert converted.hour == 12 and converted.minute == 0


# --- Date Formatting ---
def test_format_date_default():
    dt = datetime(2025, 11, 4, 14, 30, 45)
    formatted = format_date(dt)
    assert formatted.startswith("2025-11-04")

def test_format_date_custom():
    dt = datetime(2025, 11, 4, 14, 30, 45)
    fmt = "%d/%m/%Y %I:%M %p"
    assert format_date(dt, fmt) == "04/11/2025 02:30 PM"


# --- Age Calculation ---
def test_age_exact_birthday():
    birth = date(2000, 11, 4)
    today = date(2025, 11, 4)
    assert calculate_age(birth, today) == 25

def test_age_before_birthday():
    birth = date(2000, 12, 1)
    on_date = date(2025, 11, 4)
    assert calculate_age(birth, on_date) == 24

def test_age_after_birthday():
    birth = date(2000, 5, 1)
    on_date = date(2025, 11, 4)
    assert calculate_age(birth, on_date) == 25
