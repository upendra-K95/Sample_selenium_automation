import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
chrome_driver_path = os.path.join(project_path, 'drivers', 'chromedriver.exe')
# driver = webdriver.Chrome(chrome_driver_path)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.flipkart.com/')
print("Title of the Flipkart page is {} ".format(driver.title))
time.sleep(5)
driver.close()



