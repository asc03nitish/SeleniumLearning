# DropDown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def dropdown_demo():
    driver= webdriver.Chrome()

    try:
        driver.get("https://demoqa.com/select-menu")

        #old style select
        old_select= Select(driver.find_element(By.ID,"oldSelectMenu"))

        #Select by visible text
        old_select.select_by_visible_text("Green")
        time.sleep(1)

        #Select by value
        old_select.select_by_value("3")
        time.sleep(1)

        #Select by index
        old_select.select_by_index(1)
        time.sleep(1)

        #Get All Options
        options=old_select.options
        for option in options:
            print(f"Option: {option.text}")

        #Get Selected Option
        selected_option = old_select.first_selected_option
        print(f"Slected option: {selected_option.text}")

    finally:
        driver.quit()

dropdown_demo()
