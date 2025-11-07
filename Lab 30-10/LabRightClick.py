from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def right_click_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        driver.maximize_window()

        actions = ActionChains(driver)

        # Locate the button to right-click
        right_click_btn = driver.find_element(By.CSS_SELECTOR, ".context-menu-one.btn.btn-neutral")

        # Perform right click
        actions.context_click(right_click_btn).perform()
        print("Right click performed")

        time.sleep(3)

        # Verify context menu appears
        menu_option = driver.find_element(By.CSS_SELECTOR, ".context-menu-list")
        if menu_option.is_displayed():
            print("Context menu appeared successfully")

    finally:
        driver.quit()

right_click_demo()
