import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SauceDemoNavigationPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.first_product = (By.CLASS_NAME, "inventory_item_name")

    def load_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        self.driver.find_element(*self.username).send_keys("standard_user")
        self.driver.find_element(*self.password).send_keys("secret_sauce")
        self.driver.find_element(*self.login_button).click()

    def click_first_product(self):
        self.driver.find_element(*self.first_product).click()


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_page_title_changes(driver):
    page = SauceDemoNavigationPage(driver)
    page.load_login_page()
    page.login()

    time.sleep(1)
    inventory_url = driver.current_url
    first_product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    page.click_first_product()
    time.sleep(1)
    product_url = driver.current_url
    product_page_name = driver.find_element(By.CLASS_NAME, "inventory_details_name").text

    # ✅ Compare URL or Product name instead of title
    assert inventory_url != product_url, "URL did not change after clicking product"
    assert first_product_name == product_page_name, "Product name mismatch between list and detail page"
