import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




class Buttons(unittest.Testcase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_arguement('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        # driver = webdriver.Chrome(options=options)
        service_object = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service_object, options=options)
        self.driver.maximize












