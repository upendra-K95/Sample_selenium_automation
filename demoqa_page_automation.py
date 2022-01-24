import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())  # -- chrome driver installing automating
driver.maximize_window()  # -- maximizes the window

driver.get('https://demoqa.com/')  # getting in to the webpage(page url)
time.sleep(2)
print('opened chrome security gateway successfully')

'''
open_window = driver.find_element_by_id("details-button").click()
time.sleep(5)
print('clicked Advanced button successfully')


driver.find_element_by_id("proceed-link").click()
time.sleep(5)
print('clicked proceed to DemoQA successfully')
'''

driver.find_element_by_xpath("//h5[text()='Elements']").click()
# driver.find_elements_by_css_selector("#Elements')]").click()
time.sleep(3)
print('Clicked on Elements button on DemoQA Tools box')

# driver.find_element_by_class_name("//div[@class = 'header-text']").click()
# time.sleep(4)
# print("clicked Elements button ")


#driver.find_element_by_class_name("//span[@class = 'text']").click()
time.sleep(1)
print('clicked on text box in Elements drop down')

driver.find_element_by_xpath("//span[text()='Text Box']").click()
time.sleep(3)
print('selected text-box option in drop down of Elements')

driver.find_element_by_css_selector("#userName").send_keys('Upendra')
time.sleep(3)
print('successfully entered first name')

driver.find_element_by_css_selector("#userEmail").send_keys('jai.baalaiyah@gmail.com')
time.sleep(3)
print('successfully entered email')


driver.find_element_by_css_selector("#currentAddress").send_keys('H.No.-8-2-293/82/A/1355, Rd No.1, '
                                                                 'Jubilee Hills, Hyd-500033')
time.sleep(3)
print('successfully entered address')

driver.find_element_by_css_selector("#permanentAddress").send_keys('House Address: 26.4.1462/18, Chowdeswary Colony Hinoupur')
time.sleep(3)
print('successfully entered permanent address')

driver.find_element_by_id("submit").click()
time.sleep(3)
print('submitted the text form successfully')
time.sleep(2)

driver.find_element_by_xpath("//span[text() = 'Buttons']").click()
time.sleep(2)
print('selected Buttons practice page')

driver.find_elements_by_css_selector("#doubleClickBtn").click()
time.sleep(2)
print('clicked double-click button')


driver.find_elements_by_css_selector("#rightClickBtn").click()
time.sleep(2)
print('clicked right-click button')


driver.find_elements_by_css_selector("#w6U9P").click()
time.sleep(2)
print('clicked click button')

driver.close()

#   <span class="text">Text Box</span>
