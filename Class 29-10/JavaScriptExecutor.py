# Javascript Executor

from selenium import webdriver

from selenium.webdriver.common.by import By

import time


def javascript_executor_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.saucedemo.com")

        # Login first

        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        # JavaScript Executor examples

        # 1. Scroll to bottom

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

        # 2. Scroll to top

        driver.execute_script("window.scrollTo(0, 0);")

        time.sleep(2)

        # 3. Scroll to specific element

        footer = driver.find_element(By.CLASS_NAME, "footer")

        driver.execute_script("arguments[0].scrollIntoView();", footer)

        time.sleep(2)

        # 4. Highlight element

        product = driver.find_element(By.CLASS_NAME, "inventory_item_name")

        driver.execute_script("arguments[0].style.border='3px solid red'", product)

        time.sleep(2)

        # 5. Click using JavaScript

        menu_btn = driver.find_element(By.ID, "react-burger-menu-btn")

        driver.execute_script("arguments[0].click();", menu_btn)

        time.sleep(2)

        # 6. Get page title using JavaScript

        title = driver.execute_script("return document.title;")

        print(f"Page title via JS: {title}")

        # 7. Get page URL using JavaScript

        url = driver.execute_script("return document.URL;")

        print(f"Page URL via JS: {url}")



    finally:

        driver.quit()


javascript_executor_demo()

