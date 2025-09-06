
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def Open_browser(url):
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url=url)
    driver.implicitly_wait(10)

# def Click_register(locatortype,locatorpath):
#     driver.find_element(locatortype,locatorpath).click()
# //a[text()='Register']

def enter_firstname(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_lastname(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_address_street(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_address_city(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_address_state(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_address_zipcode(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_customer_ssn(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_username(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_password(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def enter_password_repeat(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def Click_register1(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def Success_message(locatortype,locatorpath,value):
    driver.find_element(locatortype,locatorpath).send_keys(value)

def close_browser():
    driver.quit()

# def click(locatortype,locatorpath):
#     driver.find_element(locatortype,locatorpath).click()
#
# def enter_text(locatortype,locatorpath, value):
#     driver.find_element(locatortype,locatorpath).send_keys(value)
