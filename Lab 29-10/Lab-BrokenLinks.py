 # Broken Links

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin, urlparse
import time


def broken_links_check():
    driver = webdriver.Chrome()

    try:

        driver.get("https://www.wikipedia.org")
         # Find all links on the page
        links = driver.find_elements(By.TAG_NAME, "a")

        print(f"Total links found: {len(links)}")

        broken_links = []

        valid_links = []

        for link in links:

            href = link.get_attribute("href")

            text = link.text.strip()

            if href:

                try:

                    # Make HEAD request to check link

                    response = requests.head(href, timeout=5)

                    if response.status_code >= 400:

                        broken_links.append((text, href, response.status_code))

                        print(f"BROKEN: {text} -> {href} (Status: {response.status_code})")

                    else:

                        valid_links.append((text, href, response.status_code))

                        print(f"VALID: {text} -> {href} (Status: {response.status_code})")



                except requests.exceptions.RequestException as e:

                    broken_links.append((text, href, f"Error: {str(e)}"))

                    print(f"BROKEN: {text} -> {href} (Error: {str(e)})")

        print(f"\nSummary:")

        print(f"Total links: {len(links)}")

        print(f"Valid links: {len(valid_links)}")

        print(f"Broken links: {len(broken_links)}")



    finally:

        driver.quit()


broken_links_check()

