# Scroll Up and Scroll Down

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


def scroll_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com/inventory.html")

        # Login first

        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        print("Scrolling methods demonstration:")

        # Method 1: Using JavaScript - Scroll by pixel

        print("1. Scrolling down by 500 pixels")

        driver.execute_script("window.scrollBy(0, 500);")

        time.sleep(2)

        print("2. Scrolling up by 300 pixels")

        driver.execute_script("window.scrollBy(0, -300);")

        time.sleep(2)

        # Method 2: Using JavaScript - Scroll to bottom

        print("3. Scrolling to bottom")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

        # Method 3: Using JavaScript - Scroll to top

        print("4. Scrolling to top")

        driver.execute_script("window.scrollTo(0, 0);")

        time.sleep(2)

        # Method 4: Using JavaScript - Scroll to specific element

        print("5. Scrolling to specific element")

        footer = driver.find_element(By.CLASS_NAME, "footer")

        driver.execute_script("arguments[0].scrollIntoView();", footer)

        time.sleep(2)

        # Method 5: Using PAGE_DOWN key

        print("6. Scrolling using PAGE_DOWN key")

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)

        time.sleep(1)

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)

        time.sleep(1)



    finally:

        driver.quit()


scroll_demo()

