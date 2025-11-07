import pytest
from selenium import webdriver
from nov4_lab.srclab.navigation_page import SauceDemoNavigationPage
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# 🧩 1️⃣ Verify Page Title Changes (Login → Inventory → Product)
def test_page_title_changes(driver):
    page = SauceDemoNavigationPage(driver)
    page.load_login_page()
    page.login()

    time.sleep(1)
    inventory_title = driver.title
    page.click_first_product()
    time.sleep(1)
    product_title = driver.title

    assert inventory_title != product_title, "Page title did not change after navigating to product"


# 🧩 2️⃣ Check URL Updates After Navigation
def test_url_updates_after_navigation(driver):
    page = SauceDemoNavigationPage(driver)
    driver.get("https://www.saucedemo.com/inventory.html")
    page.click_first_product()
    time.sleep(1)
    assert "inventory-item.html" in driver.current_url, "URL did not update correctly after navigation"


# 🧩 3️⃣ Test Back/Forward Button Functionality
def test_browser_back_forward(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    first_url = driver.current_url

    # Go into first item
    driver.find_element("class name", "inventory_item_name").click()
    time.sleep(1)
    second_url = driver.current_url

    driver.back()
    time.sleep(1)
    assert driver.current_url == first_url, "Back button did not navigate to previous page"

    driver.forward()
    time.sleep(1)
    assert driver.current_url == second_url, "Forward button did not navigate forward correctly"


# 🧩 4️⃣ Validate Breadcrumb Trail (Using Page Header as Breadcrumb)
def test_breadcrumb_simulation(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    driver.find_element("class name", "inventory_item_name").click()
    time.sleep(1)

    header = driver.find_element("class name", "inventory_details_name").text
    assert header != "", "Page header (breadcrumb-like) not found"

    driver.find_element("id", "back-to-products").click()
    time.sleep(1)
    header_back = driver.find_element("class name", "title").text

    assert header_back == "Products", "Breadcrumb (page header) not consistent after navigating back"
