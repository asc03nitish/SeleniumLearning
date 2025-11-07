# CheckBox

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def checkbox_demo():
    driver= webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/checkbox")

        #Expand Home Checkbox
        home_checkbox= driver.find_element(By.CSS_SELECTOR,".rct-checkbox")
        home_checkbox.click()
        time.sleep(2)

        #Find all checkboxes
        checkboxes=driver.find_elements(By.CSS_SELECTOR,".rct-checkbox")
        print(f"Totalcheckboxes: {len(checkboxes)}")

        #Click specific checkboxes
        for i, checkbox in enumerate(checkboxes[1:4]): #Skip for first one(home)
            checkbox.click()
            time.sleep(1)

        #Verify Selection
        selected_checkboxes= driver.find_elements(By.CSS_SELECTOR,".rct-icon-check")
        print(f"Selected checkboxes: {len(selected_checkboxes)}")

    finally:
        driver.quit()
checkbox_demo()




