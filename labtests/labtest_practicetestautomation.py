import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from labpages.lablogin_page import LoginPage
from labpages.labinventory_page import InventoryPage

class Test_practicetestautomation:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_successful_login(self, driver):
        login_page = LoginPage()
        login_page.open(driver)
        login_page.login(driver, "student", "Password123")
        inventory_page = InventoryPage()

        # Assertion 1: Check URL contains inventory
        assert "logged-in-successfully" in inventory_page.get_current_url(driver)

        # Assertion 2: Check page title is "Logged In Successfully"

        assert inventory_page.get_page_title(driver) == "Logged In Successfully"

        # Assertion 3: Logout link visible
        assert driver.find_element(*InventoryPage.LOGOUT_LINK).is_displayed()

