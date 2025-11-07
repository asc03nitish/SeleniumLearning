from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

def multi_select_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.letskodeit.com/practice")
        driver.maximize_window()

        # Locate the multi-select dropdown
        multi_select = Select(driver.find_element(By.ID, "multiple-select-example"))

        # Select multiple options
        multi_select.select_by_visible_text("Apple")
        multi_select.select_by_visible_text("Peach")
        time.sleep(1)

        # Get all selected options
        selected_options = multi_select.all_selected_options
        for option in selected_options:
            print(f"Selected option: {option.text}")

        # Deselect an option
        multi_select.deselect_by_visible_text("Apple")
        time.sleep(1)

        # Deselect all options
        multi_select.deselect_all()

    finally:
        driver.quit()

multi_select_demo()
