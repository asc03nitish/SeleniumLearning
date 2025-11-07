# Screenshot

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import os


def screenshot_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com")

        # Create screenshots directory if it doesn't exist

        if not os.path.exists("../screenshots"):
            os.makedirs("../screenshots")

            # 1. Take full page screenshot

        driver.save_screenshot("screenshots/full_page.png")

        print("Full page screenshot saved")

        # Login

        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        # 2. Take screenshot after login

        driver.save_screenshot("screenshots/after_login.png")

        print("After login screenshot saved")

        # 3. Take screenshot of specific element

        product = driver.find_element(By.CLASS_NAME, "inventory_item")

        product.screenshot("screenshots/specific_element.png")

        print("Specific element screenshot saved")



    finally:

        driver.quit()


screenshot_demo()

