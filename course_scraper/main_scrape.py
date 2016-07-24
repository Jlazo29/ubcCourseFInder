from selenium import webdriver
import sys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException


# Desc: Initialized the driver, and returns it.
# Takes: N/A
# Returns: driver (WebDriver)
def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 50)
    return driver

def go_to_CPSC(driver):
    driver.get('http://www.calendar.ubc.ca/vancouver/courses.cfm?page=code&institution=12&code=CPSC')

if __name__ == "__main__":
    driver = init_driver()
    go_to_CPSC(driver)
    time.sleep(10)
    driver.quit()
    