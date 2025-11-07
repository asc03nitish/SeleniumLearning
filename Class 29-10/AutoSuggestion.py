# Auto Suggestions

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


def auto_suggestion():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.google.com")

        # Find search box and enter text

        search_box = driver.find_element(By.NAME, "q")

        search_box.send_keys("selenium")

        time.sleep(2)  # Wait for suggestions to appear

        # Get all suggestions

        suggestions = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li")

        print(f"Number of suggestions: {len(suggestions)}")

        # Print all suggestions

        for i, suggestion in enumerate(suggestions):

            text = suggestion.text

            if text:
                print(f"{i + 1}. {text}")

                # Click on the first suggestion

        if suggestions:
            suggestions[0].click()

            time.sleep(2)



    finally:

        driver.quit()


auto_suggestion() 

