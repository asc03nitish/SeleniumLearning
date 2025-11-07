# Radio Button

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def radio_button_demo():
    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/radio-button")

        # Find radio buttons
    yes_radio = driver.find_element(By.ID, "yesRadio")
    impressive_radio = driver.find_element(By.ID, "impressiveRadio")
    no_radio = driver.find_element(By.ID, "noRadio")



# Click radio button using JavaScript (if direct click doesn't work)

    driver.execute_script("arguments[0].click();", yes_radio)
    #yes_radio.click()
    time.sleep(2)

# Check if selected
    success_text=driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/p/span").text
    print(f"Success text: {success_text}")
    if(success_text.lower() in "yes"):
        print("Success text matches exactly!")
    else:
        print(f"Success text DONT match")
    is_selected = driver.execute_script("return arguments[0].checked;", yes_radio)
    print(f"Yes radio selected: {is_selected}")

# Click another radio button

    driver.execute_script("arguments[0].click();", impressive_radio)
    time.sleep(2)

    is_selected = driver.execute_script("return arguments[0].checked;", impressive_radio)

    print(f"Impressive radio selected: {is_selected}")

    driver.quit()

radio_button_demo()