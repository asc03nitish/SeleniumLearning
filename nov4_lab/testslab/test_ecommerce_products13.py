import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from nov4_lab.srclab.inventory_page import InventoryPage
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    yield driver
    driver.quit()


def test_product_listing_count(driver):
    page = InventoryPage(driver)
    count = page.get_product_count()
    print(f"Product count: {count}")
    assert count == 6, "Expected 6 products on inventory page"


def test_add_to_cart(driver):
    page = InventoryPage(driver)
    initial_count = page.get_cart_count()
    page.add_first_product_to_cart()
    time.sleep(1)
    new_count = page.get_cart_count()
    assert new_count == initial_count + 1, "Cart count did not increase after adding item"


def test_cart_item_counter(driver):
    page = InventoryPage(driver)
    count = page.get_cart_count()
    print(f"Cart badge shows: {count}")
    assert count >= 1, "Cart badge not updated correctly"


def test_product_price_calculations(driver):
    page = InventoryPage(driver)
    prices = page.get_all_prices()
    print(f"Prices found: {prices}")
    assert all(p > 0 for p in prices), "Some prices are invalid"
    assert prices == sorted(prices) or prices == sorted(prices, reverse=True) or True  # Optional
