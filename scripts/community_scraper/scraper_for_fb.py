"""Scrapes give FaceBook Communities for Emails"""

import logging
import os
from pathlib import Path
from time import sleep
from selenium.webdriver.common.by import By

from helpers import ScrapeEmails, GetChromeDriver

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def scrape_fb_communities(time_str: str, output_dir_path: str, user: str, password: str, communities_list: str, scroll_depth: str, master_email_file: str):
    # setup logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # main logic
    logger.debug("Logging into Facebook")
    driver = GetChromeDriver()
    driver.get('https://www.facebook.com/')
    driver.maximize_window()
    sleep(1)

    username_box = driver.find_element(By.ID, 'email')
    username_box.send_keys(user)

    password_box = driver.find_element(By.ID, 'pass')
    password_box.send_keys(password)

    login_box = driver.find_element(By.NAME, 'login')
    # login_box = driver.find_element(By.XPATH, "input[starts-with(@id, 'u_0_')][@value='Log In']")
    # login_box = driver.find_element_by_xpath("//input[starts-with(@id, 'u_0_')][@value='Log In']")
    login_box.click()
    sleep(4)
    
    # Now we should be logged into FaceBook, we can start scraping the provided communities
    scroll_depth = int(scroll_depth)
    scraped_emails = set()
    with open(communities_list, "r") as communities:
        for community in communities.readlines():
            logger.info(f'Scraping {community}')
            emails = ScrapeEmails(driver=driver, target_url = community, scroll_depth = scroll_depth)

            logger.info(f"Emails Found from {community} : {emails}")
            scraped_emails.update(emails)

    
    # Writing output to master and output files
    with open(master_email_file, "r") as main_email_file:
        master_emails = set(email.strip() for email in main_email_file.readlines())

    with open(master_email_file, "w") as main_email_file:
        master_emails.update(scraped_emails)
        for email in master_emails:
            main_email_file.write(f"{email}{os.linesep}")

    output_path = Path(output_dir_path) / "facebook_scraped_emails.txt"
    with open(output_path, "w") as output_file:
        for email in scraped_emails:
            output_file.write(f"{email}{os.linesep}")

    driver.quit()