"""Returns an already configured chrome webdriver"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

def get_chrome_driver():
    options = Options()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2           
            # with 2 should disable notifications
        },
    )
    options.add_argument('--disable-notifications') 
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver