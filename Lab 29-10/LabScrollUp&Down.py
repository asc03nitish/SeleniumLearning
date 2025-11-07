from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def scroll_demo():
    driver = webdriver.Chrome()

    try:
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()
        time.sleep(2)

        print("Scrolling demonstration on alternate website:")

        # Method 1: Scroll down by pixel
        print("1. Scrolling down by 600 pixels")
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        # Method 2: Scroll up by pixel
        print("2. Scrolling up by 400 pixels")
        driver.execute_script("window.scrollBy(0, -400);")
        time.sleep(2)

        # Method 3: Scroll to bottom of the page
        print("3. Scrolling to bottom")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Method 4: Scroll to top of the page
        print("4. Scrolling to top")
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        # Method 5: Scroll to a specific element
        print("5. Scrolling to a specific element (Table)")
        element = driver.find_element(By.XPATH, "//table[@name='BookTable']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(2)

        # Method 6: Scroll using PAGE_DOWN and PAGE_UP keys
        print("6. Scrolling using PAGE_DOWN and PAGE_UP keys")
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_UP)
        time.sleep(1)

        print("Scroll demo completed successfully.")

    finally:
        driver.quit()


scroll_demo()
