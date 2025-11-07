from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def explicit_wait_demo():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Login
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        # Wait until the success message is visible
        success_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='loop-container']//p"))
        )
        print("Login successful message:", success_message.text)

        # Wait for URL change
        wait.until(EC.url_contains("logged-in-successfully"))
        print("Navigated to success page")

    finally:
        driver.quit()

explicit_wait_demo()
