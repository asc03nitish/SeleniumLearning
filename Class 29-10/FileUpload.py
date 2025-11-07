 # File Upload

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

import os


def file_upload_sendkeys():
    driver = webdriver.Chrome()

    try:

        driver.get("https://the-internet.herokuapp.com/upload")

        # Create a test file to upload

        with open("../test_upload.txt", "w") as f:

            f.write("This is a test file for upload")

             # Upload file using send_keys

        file_input = driver.find_element(By.ID, "file-upload")

        file_input.send_keys(os.path.abspath("../test_upload.txt"))

        # Click upload button

        upload_btn = driver.find_element(By.ID, "file-submit")

        upload_btn.click()

        time.sleep(2)

        # Verify upload success

        success_message = driver.find_element(By.TAG_NAME, "h3").text

        print(f"Upload result: {success_message}")

        # Clean up

        # if os.path.exists("test_upload.txt"):
        #     os.remove("test_upload.txt")



    finally:

        driver.quit()


file_upload_sendkeys()