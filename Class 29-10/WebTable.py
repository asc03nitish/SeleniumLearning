# Web Table

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def web_table_demo():
    driver = webdriver.Chrome()

    try:

        driver.get("https://demoqa.com/webtables")

        # Get all rows in the table

        rows = driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")

        print(f"Total rows: {len(rows)}")

        # Extract data from each row

        for i, row in enumerate(rows):

            cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")

            if len(cells) >= 6:  # Ensure we have enough cells

                row_data = [cell.text for cell in cells[:6]]  # First 6 columns

                if any(row_data):  # Skip empty rows

                    print(f"Row {i + 1}: {row_data}")

                    # Find specific data

        for row in rows:

            cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")

            if len(cells) >= 4 and cells[0].text == "Cierra":
                print(f"Found Cierra: {cells[3].text}")  # Department

                break



    finally:

        driver.quit()


web_table_demo()

