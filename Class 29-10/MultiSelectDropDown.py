# Multi-Select DropDown
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def multi_select_demo():
    driver= webdriver.Chrome()

    try:
        driver.get("https://demoqa.com/select-menu")

        #Multi-Select DropDown
        multi_select = Select(driver.find_element(By.ID,"cars"))

        #Select Multiple Options
        multi_select.select_by_visible_text("Volvo")
        multi_select.select_by_visible_text("Audi")
        time.sleep(1)

        #Get all selected options
        selected_options=multi_select.all_selected_options
        for option in selected_options:
            print(f"Selected option: {option.text}")

        #Deselect an option
        multi_select.deselect_by_visible_text("Volvo")
        time.sleep(1)

        #Deselect All
        multi_select.deselect_all()

    finally:
        driver.quit()

multi_select_demo()