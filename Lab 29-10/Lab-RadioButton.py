from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def radio_button_demo():
    driver = webdriver.Chrome()

    try:
        # Open alternate practice site
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()

        # Scroll to bring radio buttons into view
        driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(2)

        # Locate radio buttons for gender
        male_radio = driver.find_element(By.XPATH, "//input[@id='male']")
        female_radio = driver.find_element(By.XPATH, "//input[@id='female']")

        # Click Male radio
        driver.execute_script("arguments[0].click();", male_radio)
        time.sleep(1)

        # Verify selection
        male_selected = driver.execute_script("return arguments[0].checked;", male_radio)
        female_selected = driver.execute_script("return arguments[0].checked;", female_radio)
        print(f"Male selected: {male_selected}, Female selected: {female_selected}")

        # Click Female radio
        driver.execute_script("arguments[0].click();", female_radio)
        time.sleep(1)

        # Verify again
        male_selected = driver.execute_script("return arguments[0].checked;", male_radio)
        female_selected = driver.execute_script("return arguments[0].checked;", female_radio)
        print(f"Male selected: {male_selected}, Female selected: {female_selected}")

    finally:
        driver.quit()


radio_button_demo()
