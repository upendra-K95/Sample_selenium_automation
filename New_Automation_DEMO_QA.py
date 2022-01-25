import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get('https://demoqa.com/')
time.sleep(2)
print('opened DEMO-QA successfully')

driver.find_element_by_xpath("//h5[text()='Elements']").click()
time.sleep(2)
print('Selected Elements on DemoQA Tools box')

driver.find_element_by_xpath("//span[text()='Text Box']").click()
time.sleep(2)
print('Text-box option in Elements')

driver.find_element_by_css_selector("#userName").send_keys('Upendra')
time.sleep(2)
print('successfully entered first name')

driver.find_element_by_css_selector("#userEmail").send_keys('jai.baalaiyah@gmail.com')
time.sleep(2)
print('successfully entered email')

driver.find_element_by_css_selector("#currentAddress").send_keys('H.No.-8-2-293/82/A/1355, Rd No.1, '
                                                                 'Jubilee Hills, Hyd-500033')
time.sleep(2)
print('successfully entered address')

driver.find_element_by_css_selector("#permanentAddress").send_keys('House Address: 26.4.1462/18, Chowdeswary Colony '
                                                                   'Hindupur')
time.sleep(2)
print('successfully entered permanent address')

driver.find_element_by_id("submit").click()
time.sleep(2)
print('submitted the text form successfully')
print('*'*90)

driver.find_element_by_xpath("//span[text()='Check Box']").click()
time.sleep(2)
print('selected Check-box option in Elements')

driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
time.sleep(2)
print('selected Check-box home')

driver.find_element_by_class_name("rct-checkbox").click()
time.sleep(2)
print("Checked Check-box's Home")

driver.find_element_by_xpath("//span[text()='Radio Button']").click()
time.sleep(1)
print('selected is Radio button')

radio_button = driver.find_element_by_xpath("//label[text()='Yes']").click()
time.sleep(2)
print("selected yes Radio button")

driver.find_element_by_xpath("//span[text()='Web Tables']").click()
time.sleep(2)
print('Web tables is selected ')

open_window = driver.find_element_by_id('addNewRecordButton').click()
active_windows = driver.window_handles
print(f"ADD button is selected in window = {active_windows}")

for window in active_windows:
    time.sleep(2)
    driver.switch_to.window(window)
    # print('switch to windows is working')
    if window.title == 'Registration Form':
        print('if condition for registration form is working')

        if driver.find_element_by_css_selector == "[id='firstName']":
            driver.click()
            time.sleep(2)
            driver.send_keys('Upendra')
            print('written firstname in the form')

        if driver.find_element_by_css_selector == "[id='lastName']":
            driver.click()
            time.sleep(2)
            driver.send_keys('kotipalli')
            print('written lastname in the form')

        if driver.find_element_by_css_selector == "[id='userEmail']":
            driver.click()
            time.sleep(2)
            driver.send_keys('jai.baalaiyah@gmail.com')
            print('written email in the form')

        if driver.find_element_by_css_selector == "[id = 'age']":
            driver.click()
            time.sleep(2)
            driver.send_keys('17')
            print('written age in the form')

        if driver.find_element_by_css_selector == "[id='salary']":
            driver.click()
            time.sleep(2)
            driver.send_keys('100000000')
            print('written salary in the form')

        if driver.find_element_by_css_selector == "[id = 'department']" :
            driver.click()
            time.sleep(2)
            driver.send_keys('FIRE')
            print('written Department in the form')

        if driver.find_element_by_css_selector == "[id='submit']":
            driver.click()
            time.sleep(2)
            print('Submitted the form successfully')

            print('entered all the web table details and successfully submitted')


print('Successfully opened Window ADD and performed submit form')


driver.close()



'''
driver.find_element_by_xpath("//*[text()='Elements']").click()
time.sleep(2)
print('Reselected Elements')

'''
'''
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
'''

'''driver.find_element_by_xpath("//span[text() = 'Buttons']").click()
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

'''
open_window = driver.find_element_by_id("details-button").click()
time.sleep(5)
print('clicked Advanced button successfully')


driver.find_element_by_id("proceed-link").click()
time.sleep(5)
print('clicked proceed to DemoQA successfully')
'''
