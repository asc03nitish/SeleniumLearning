from selenium import webdriver
from selenium.webdriver.common.by import By

def implicit_wait_demo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "submit")

        username.send_keys("student")
        password.send_keys("Password123")
        login_btn.click()

    finally:
        driver.quit()

implicit_wait_demo()
