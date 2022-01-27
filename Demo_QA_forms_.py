import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
driver.get('https://demoqa.com/')
print('opened DEMO-QA successfully')

driver.execute_script("window.scrollBy(0,250)", "")
driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div[2]/div/div[3]").click()
time.sleep(2)
print('Selected Forms on DemoQA Tools box')
driver.find_element(By.XPATH, "(//*[@id='item-0']/span)[2]").click()
time.sleep(2)
print('Prcatice Forms Page selected')
driver.execute_script("window.scrollBy(0,170)", "")
driver.find_element(By.ID, "firstName").send_keys('Upendra')
time.sleep(2)
driver.find_element(By.ID, "lastName").send_keys('Kotipalli')
driver.find_element(By.ID, "userEmail").send_keys('Jai.baalaiyah@gmail.com')
radio_button = driver.find_element_by_xpath("//input[@id='gender-radio-1']").is_selected()
print('radio button is selected')
driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys('9704400123')
driver.find_element(By.ID, "dateOfBirthInput").send_keys("02 Oct 2022")
# print('subjects')

# element = driver.is_selected()
# drop = Select(driver.find_element(By.XPATH,"//*[@id='subjectsWrapper']/div[2]"))
driver.find_element(By.XPATH, "//*[@id='subjectsContainer']/div").click()
# drop_2.select_by_value(2)
print('subjects2')
driver.find_element(By.ID, "subjectsContainer").click()
# driver.find_element(By.XPATH,"//input[@id='uploadPicture']").click()
# driver.switch_to_frame(0)
element_2 = driver.find_element(By.XPATH, "//*[@id='userForm']/div[8]/div[2]/div/input")
print('subjects2')
# element_2.send_keys("C://Users//Rebel Upendra//Downloads//sampleFile.jpg")
print('upload button')
driver.execute_script("window.scrollBy(0,230)", "")
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys('H.No.-8-2-293/82/A/1355, Rd No.1, '
                                                                 'Jubilee Hills, Hyd-500033 ')
# element_2 C:\Users\Rebel Upendra\Downloads
print('upload button2')
element_3 = driver.find_element(By.ID,'react-select-3-input')
drop = Select(element_3)
print(len(drop.options))
# element_3.select_by_visible_text('Uttar Pradesh')

driver.find_elements_by_id("submit")
# driver.execute_script("window.scrollBy(0,100)", "")
time.sleep(2)
driver.close()
