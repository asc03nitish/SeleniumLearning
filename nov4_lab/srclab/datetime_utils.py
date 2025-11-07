# Experiments/src/datetime_utils.py
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo


# --- Date Comparisons and Differences ---
def days_between(date1: date, date2: date) -> int:
    """Return the absolute number of days between two dates."""
    return abs((date2 - date1).days)


# --- Timezone Conversions ---
def convert_timezone(dt: datetime, from_tz: str, to_tz: str) -> datetime:
    """Convert a datetime from one timezone to another using zoneinfo."""
    # Attach source timezone and convert to target
    dt = dt.replace(tzinfo=ZoneInfo(from_tz))
    return dt.astimezone(ZoneInfo(to_tz))


# --- Date Formatting ---
def format_date(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime according to the given format string."""
    return dt.strftime(fmt)


# --- Age Calculation ---
def calculate_age(birth_date: date, on_date: date = None) -> int:
    """Calculate age in years as of a specific date."""
    if on_date is None:
        on_date = date.today()
    age = on_date.year - birth_date.year
    if (on_date.month, on_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
