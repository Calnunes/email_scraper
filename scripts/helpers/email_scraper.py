"""Scrapes emails from the provided website"""

from selenium import webdriver
from time import sleep
import re

def scrape_emails(driver: webdriver.Chrome, target_url: str, scroll_depth: int):
    driver.get(target_url)
    count = 0
    while count < scroll_depth:
        count += 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
    html = driver.page_source
    emails = re.findall(email_pattern, html)
    return emails