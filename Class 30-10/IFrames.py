from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def frame_handling_demo():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()

    try:
        # Switch to frame by ID
        driver.switch_to.frame("frame1")
        print("Switched to frame1")

        # Get text inside the frame
        frame_text = driver.find_element(By.ID, "sampleHeading").text
        print(f"Frame text from frame1: {frame_text}")

        # Switch back to main content
        driver.switch_to.default_content()
        print("Switched back to main content")

        # Switch to second frame by WebElement
        frame2_element = driver.find_element(By.ID, "frame2")
        driver.switch_to.frame(frame2_element)
        print("Switched to frame2")

        frame_text2 = driver.find_element(By.ID, "sampleHeading").text
        print(f"Frame text from frame2: {frame_text2}")

    finally:
        time.sleep(2)
        driver.quit()

frame_handling_demo()

# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# import time
#
#
# def frame_handling_demo():
#     driver = webdriver.Chrome()
#
#     try:
#
#         driver.get("https://demoqa.com/frames")
#
#         # Switch to frame by index
#
#         driver.switch_to.frame(0)
#
#         print("Switched to frame 0")
#
#         # Get text from frame
#
#         frame_text = driver.find_element(By.ID, "sampleHeading").text
#
#         print(f"Frame text: {frame_text}")
#
#         # Switch back to main content
#
#         driver.switch_to.default_content()
#
#         print("Switched back to main content")
#
#         # Switch to frame by ID/Name (if available)
#
#         # driver.switch_to.frame("frame1")
#
#         # Switch to frame by WebElement
#
#         frame_element = driver.find_element(By.ID, "frame1")
#
#         driver.switch_to.frame(frame_element)
#
#         print("Switched to frame by element")
#
#         frame_text = driver.find_element(By.ID, "sampleHeading").text
#
#         print(f"Frame text: {frame_text}")
#
#         # Always switch back to default content
#
#         driver.switch_to.default_content()
#
#
#
#     finally:
#
#         driver.quit()
#
#
# frame_handling_demo() 