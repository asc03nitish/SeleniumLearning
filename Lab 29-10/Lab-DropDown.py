from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def dropdown_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.letskodeit.com/practice")
        driver.maximize_window()

        dropdown = Select(driver.find_element(By.ID, "carselect"))

        dropdown.select_by_visible_text("Benz")
        time.sleep(1)

        dropdown.select_by_value("honda")
        time.sleep(1)

        dropdown.select_by_index(0)
        time.sleep(1)

        # Print all options
        for option in dropdown.options:
            print(f"Option: {option.text}")

        # Print selected option
        print(f"Selected option: {dropdown.first_selected_option.text}")

    finally:
        driver.quit()

dropdown_demo()
