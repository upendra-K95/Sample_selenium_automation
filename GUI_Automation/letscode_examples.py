# -------------- Finding the Elements by ID's ------------

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

'''

# here using Radio button 
driver = webdriver.Chrome(ChromeDriverManager().install()) # -- chrome driver installing automating
driver.maximize_window() # -- maximizes the window
driver.get('https://courses.letskodeit.com/practice') # getting in to the webpage(page url)
radio_button = driver.find_element_by_id('benzradio') # -- finding the element by id
radio_button.click() # -- click function 
radio_button.is_selected() # -- 'is' enabled selection method
time.sleep(6) # -- time delay for webpage preview
print("Radio button is clicked") 
driver.close() # -- closing the webpage 

# here using Check box button
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://courses.letskodeit.com/practice')
Check_box_button = driver.find_element_by_id('hondacheck')
Check_box_button.click()
Check_box_button.is_selected()
time.sleep(6)
print("Check box button is Clicked")
driver.close()

# here using Radio button & Check box button
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://courses.letskodeit.com/practice')
radio_button =driver.find_element_by_id('benzradio')
Check_box =driver.find_element_by_id('hondacheck')
radio_button.click()
Check_box.click()
radio_button.is_selected()
Check_box.is_selected()
time.sleep(6)
print("Radio button is clicked & Checkbox is Clicked")
driver.close()


# here using text_box
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://courses.letskodeit.com/practice')
text_box = driver.find_element_by_id('displayed-text')
text_box.send_keys("Upsii")
time.sleep(6)
print("Successfully entered text in Text box")
driver.close()


# here using drop down button
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://courses.letskodeit.com/practice')
select_tag = Select(driver.find_element_by_id('carselect'))
select_tag.select_by_index(2)
time.sleep(3)
select_tag.select_by_value('benz')
time.sleep(3)
select_tag.select_by_visible_text('BMW')
time.sleep(3)
print("Successfully selected text in Text box")
driver.close()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://courses.letskodeit.com/practice')
Multiple_select_tag = Select(driver.find_element_by_name('multiple-select-example'))
Multiple_select_tag.select_by_index(2)
time.sleep(3)
Multiple_select_tag.select_by_value('orange')
time.sleep(3) 
Multiple_select_tag.select_by_visible_text('APPLE')
driver.close()
print('Successfully selected Multiple-Select-tags')
'''

# clicking new window
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://courses.letskodeit.com/practice')
open_window = driver.find_element_by_id('openwindow').click()
active_windows = driver.window_handles
print(active_windows)
for window in active_windows:
    time.sleep(3)
    driver.switch_to.window(window)
    if driver.title == 'All Courses':
        driver.find_element_by_xpath("//*[@href='/login']").click()
        time.sleep(3)
        print('*'*50)

print('Successfully opened Window inside a button and performed Click action')
