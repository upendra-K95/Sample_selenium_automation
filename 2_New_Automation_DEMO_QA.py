import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get('https://demoqa.com/')
print('opened DEMO-QA successfully')

driver.execute_script("window.scrollBy(0,200)", "")
driver.find_element_by_xpath("//h5[text()='Elements']").click()
print('Selected Elements on DemoQA Tools box')
driver.execute_script("window.scrollBy(0,100)", "")
driver.find_element_by_xpath("//span[text()='Text Box']").click()
print('Text-box option in Elements')
driver.find_element_by_css_selector("#userName").send_keys('Upendra')
print('successfully entered first name')
driver.find_element_by_css_selector("#userEmail").send_keys('jai.baalaiyah@gmail.com')
print('successfully entered email')
driver.execute_script("window.scrollBy(0,300)", "")
driver.find_element_by_css_selector("#currentAddress").send_keys('H.No.-8-2-293/82/A/1355, Rd No.1, '
                                                                 'Jubilee Hills, Hyd-500033')
print('successfully entered Current address')
driver.execute_script("window.scrollBy(0,300)", "")
driver.find_element_by_css_selector("#permanentAddress").send_keys('House Address: 26.4.1462/18, Chowdeswary Colony '
                                                                   'Hindupur')
print('successfully entered permanent address')
driver.find_element_by_id("submit").click()
driver.execute_script("window.scrollBy(0,200)", "")
print('submitted the text form successfully')
driver.find_element_by_xpath("//span[text()='Check Box']").click()
driver.execute_script("window.scrollBy(0,50)", "")
print('selected Check-box option in Elements')
driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
print('selected Check-box home')
driver.find_element_by_class_name("rct-checkbox").click()
print("Checked in Check-box's Home")
driver.find_element_by_xpath("//span[text()='Radio Button']").click()
print('selected is Radio button')
radio_button = driver.find_element_by_xpath("//label[text()='Yes']").click()
driver.execute_script("window.scrollBy(0,200)", "")
print("selected yes Radio button")
driver.find_element_by_xpath("//span[text()='Web Tables']").click()
print('Web tables is selected ')
open_window = driver.find_element_by_id('addNewRecordButton').click()
active_windows = driver.window_handles
print(f"ADD button is selected in window = {active_windows}")
for window in active_windows:
    driver.switch_to.window(window)
    print(driver.title)
    print('switch to windows is working')
    if driver.title == driver.title:
        print('if condition for registration form is working')
        driver.find_element_by_css_selector("[id='firstName']").send_keys('Upendra')
        print('written firstname in the form')

        driver.find_element_by_css_selector("[id='lastName']").send_keys('kotipalli')
        print('written lastname in the form')

        driver.find_element_by_css_selector("[id='userEmail']").send_keys('jai.baalaiyah@gmail.com')
        print('written email in the form')

        driver.find_element_by_css_selector("[id = 'age']").send_keys('17')
        print('written age in the form')

        driver.find_element_by_css_selector("[id='salary']").send_keys('100000000')
        print('written salary in the form')

        driver.find_element_by_css_selector("[id = 'department']").send_keys('FIRE')
        print('written Department in the form')

        driver.find_element_by_css_selector("[id='submit']").click()
        print('Submitted the form successfully')
        time.sleep(1)
driver.execute_script("window.scrollBy(0,300)", "")
print('entered all the web table details and successfully submitted')
driver.find_element_by_xpath("//*[@id='item-4']/span").click()
driver.execute_script("window.scrollBy(0,300)", "")
element = driver.find_element_by_xpath("//*[@id='item-4']/span")
actions = ActionChains(driver)
actions.double_click(element).perform()
print("performed double click()")
actions_2 = ActionChains(driver)
element2 = driver.find_element_by_xpath("//*[@id='rightClickBtn']")
actions_2.context_click(element2).perform()
print("performed right click()")
driver.find_element_by_xpath("//button[text()='Click Me']").click()
print('performed dynamic click')
driver.execute_script("window.scrollBy(0,200)", "")
print('Successfully Registered Details and Performed submit form')
driver.execute_script("window.scrollBy(0,250)", "")
driver.find_element_by_xpath("//*[@id='item-5']/span").click()
print('selected Links')
driver.find_element_by_xpath("//*[@id='simpleLink']").click()
print(driver.current_window_handle)  # -- returns Current window handle[parent window]
handles = driver.window_handles  # returns all the browser values of opened browser windows
# handle: object
for handle in handles:
    driver.switch_to.window(handle)
    print(f"printing the titles here -- {driver.title}")
    print(driver.switch_to.window)
    time.sleep(1)
    print('switched to new window')

    driver.execute_script("window.scrollBy(0,100)", "")
    driver.find_element_by_xpath("//h5[text()='Elements']").click()
    print('Selected Elements on DemoQA Tools box')
    driver.execute_script("window.scrollBy(0,100)", "")
    driver.close()

#        quit()

driver.close()
