"""
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
chrome_driver_path = os.path.join(project_path, 'drivers', 'chromedriver.exe')
chrome_driver_path.get("https://www.amazon.in/ref=nav_logo")
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Amazon page Title -- {}".format(driver.title))
# driver.close()
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.amazon.in/ref=nav_logo')
print("Amazon page Title -- {}".format(driver.title))
time.sleep(6)

driver.close()
