import pytest
from selenium import webdriver
from nov4_lab.srclab.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# 🧩 1️⃣ Required Field Validation
def test_required_fields(driver):
    page = LoginPage(driver)
    page.load()
    page.login("", "")  # no username and password

    error = page.get_error_message()
    assert "Username is required" in error, "Required field validation failed"


# 🧩 2️⃣ Invalid Email Format (simulate incorrect username format)
def test_invalid_email_format(driver):
    page = LoginPage(driver)
    page.load()
    page.login("invalidemail@", "secret_sauce")

    # Saucedemo treats all as username, but we can validate a failed login
    error = page.get_error_message()
    assert "do not match any user" in error.lower(), "Invalid username format not handled properly"


# 🧩 3️⃣ Password Confirmation (simulate wrong password)
def test_password_mismatch(driver):
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "wrongPassword")

    error = page.get_error_message()
    assert "do not match any user" in error.lower(), "Wrong password not handled properly"


# 🧩 4️⃣ Successful Login
def test_successful_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("standard_user", "secret_sauce")

    # After login, verify we reach inventory page
    assert "inventory.html" in driver.current_url, "User not redirected to products page after successful login"
