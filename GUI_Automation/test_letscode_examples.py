import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver_initialise():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://courses.letskodeit.com/practice')
    driver.maximize_window()
    yield driver
    driver.close()


def test_radio_button(driver_initialise):
    radio_button = driver_initialise.find_element_by_id('benzradio')
    radio_button.click()
    radio_button.is_selected()
    time.sleep(6)
    print("Radio button is clicked")
    assert radio_button.is_selected() == True


def test_Check_box_button(driver_initialise):
    Check_box_button = driver_initialise.find_element_by_id('hondacheck')
    Check_box_button.click()
    Check_box_button.is_selected()
    time.sleep(6)
    print("Check box button is Clicked")
    assert Check_box_button.is_selected() == True


def test_text_box_button(driver_initialise):
    text_box = driver_initialise.find_element_by_id('displayed-text')
    text_box.send_keys("Upsii")
