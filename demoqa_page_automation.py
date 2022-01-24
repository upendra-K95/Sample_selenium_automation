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

# time.sleep(4)
# print("clicked Elements button ")


# driver.find_element_by_class_name("//span[@class = 'text']").click()
# time.sleep(1)
# print('clicked on text box in Elements drop down')

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

driver.find_element_by_class_name("//span[@class='pr-1']/preceding::div[10]").click()
time.sleep(2)
print('*'*90)

driver.find_element_by_xpath("//div[@class='element-group']/following::div[3]").click()
time.sleep(2)
print('selected Forms')


driver.find_element_by_xpath("//div[@class='element-list collapse show']/descendant::span").click()
time.sleep(2)
print('selected practice Form')

driver.find_element_by_id("firstName").send_keys('Upendra')
time.sleep(2)
print('entered first-name successfully into form')

driver.find_element_by_id("lastName").send_keys('Kotipalli')
time.sleep(2)
print('entered last-name successfully into form')

driver.find_element_by_xpath("//input[@id='userEmail']").send_keys('jai.baalaiyah@gmail.com')
time.sleep(2)
print('entered gmail successfully into form')


radio_button = driver.find_element_by_xpath("//label[text()='Male']").click()
radio_button.is_selected()
time.sleep(2)
print("Gender Radio button is clicked")

driver.find_element_by_xpath("//input[@id='userNumber']").send_keys('9704400123')
time.sleep(2)
print("Mobile Number entered")



driver.close()

#   <span class="text">Text Box</span>
#//div[@class = 'header-text']/following-sibling::div

'''
driver.find_element_by_xpath("//span[text() = 'Buttons']").click()
time.sleep(2)
print('selected Buttons practice ')

driver.find_elements_by_css_selector("#doubleClickBtn").click()
time.sleep(2)
print('clicked double-click button')


driver.find_elements_by_css_selector("#rightClickBtn").click()
time.sleep(2)
print('clicked right-click button')


driver.find_elements_by_css_selector("#w6U9P").click()
time.sleep(2)
print('clicked click button')
'''
