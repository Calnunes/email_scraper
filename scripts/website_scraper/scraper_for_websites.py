"""Scrapes a list of websites for emails"""
import logging
import os
from pathlib import Path

from helpers import ScrapeEmails, GetChromeDriver

def scrape_websites(time_str: str, output_dir_path: str, websites_list: str, scroll_depth: str, master_email_file: str):
    # setup logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # main logic
    scroll_depth = int(scroll_depth)
    scraped_emails = set()
    with open(websites_list, "r") as websites:
        for website in websites.readlines():
            logger.info(f'Scraping {website}')
            emails = ScrapeEmails(driver=GetChromeDriver(), target_url = website, scroll_depth = scroll_depth)

            logger.info(f"Emails Found from {website} : {emails}")
            scraped_emails.update(emails)

    # print(scraped_emails)
    
    with open(master_email_file, "r") as main_email_file:
        master_emails = set(email.strip() for email in main_email_file.readlines())

    with open(master_email_file, "w") as main_email_file:
        master_emails.update(scraped_emails)
        for email in master_emails:
            main_email_file.write(f"{email}{os.linesep}")

    output_path = Path(output_dir_path) / "website_scraped_emails.txt"
    with open(output_path, "w") as output_file:
        for email in scraped_emails:
            output_file.write(f"{email}{os.linesep}")

    