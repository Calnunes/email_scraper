import configparser
import os
import logging
import datetime

from website_scraper.scraper_for_websites import scrape_websites
from community_scraper.scraper_for_fb import scrape_fb_communities

# ----------------------------- Configure Global Logger -----------------------------
logger = logging.getLogger("root")
logger.setLevel(logging.INFO)

# Setup File Handler
now = datetime.datetime.now()
time_str = now.strftime('%Y-%m-%d-%H-%M-%S')

current_file_path = os.path.abspath(__file__)
logfile_path = os.path.join(os.path.dirname(current_file_path), f'../logs/logfile_{time_str}.log')

file_handler = logging.FileHandler(logfile_path)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# ----------------------------- Parsing the Config File --------------------------------------------
parser = configparser.ConfigParser()

# Get the path to the current file
current_file_path = os.path.abspath(__file__)
# Get the path to the configuration file
config_file_path = os.path.join(os.path.dirname(current_file_path), '../config_file')


parser.read(config_file_path)
for sect in parser.sections():
    if sect == "website_scraper":
        website_scraper_configs = {k:v for (k,v) in parser.items(sect)}
    elif sect == "fb_community_scraper":
        fb_community_scraper_configs = {k:v for (k,v) in parser.items(sect)}
    # for k,v in parser.items(sect):
    #     print(' {} = {}'.format(k,v))
    # print()

# ----------------------------- Create output directory with OUTPUT -------------------------------------- 
current_file_path = os.path.abspath(__file__)
output_dir_path = os.path.join(os.path.dirname(current_file_path), f'../OUTPUT/output_{time_str}')
os.mkdir(output_dir_path)
# output_dir = 

# ----------------------------- Scrape Websites for emails --------------------------------------
# print(website_scraper_configs)
scrape_websites(time_str=time_str, output_dir_path=output_dir_path, **website_scraper_configs)


# ----------------------------- Scrape Facebook Communities for emails -----------------------------
# print(fb_community_scraper_configs)
scrape_fb_communities(time_str=time_str, output_dir_path=output_dir_path, **fb_community_scraper_configs)