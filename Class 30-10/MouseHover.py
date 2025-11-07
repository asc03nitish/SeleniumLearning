from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/menu")

# Remove floating ads and iframes that may block interaction
driver.execute_script("document.querySelector('#fixedban')?.remove();")
driver.execute_script("document.querySelectorAll('iframe').forEach(a => a.remove());")

actions = ActionChains(driver)

main_item = driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/a")
actions.move_to_element(main_item).perform()
time.sleep(1)

sub_item = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
actions.move_to_element(sub_item).perform()
time.sleep(1)

driver.quit()