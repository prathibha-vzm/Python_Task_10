#Importing Packages

import time
import pytest
from selenium.webdriver.common.by import By


#Positive-test case -> Fetch the home page URL
# 19 & 22 : Used Name locator to find and inputing values
# 24:Using currenturl to fetch the URL and (31:) checking it using assert
# 26: Used ID locator and clicked on the button element 
# 14:marking for sanity test

@pytest.mark.sanity
def test_valid_current_login_url(driver_method):

    driver = driver_method

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    url = driver.current_url

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    print("URL of this Page is ", url)

    assert url == 'https://www.saucedemo.com/'


#Negative-test case -> Fetching Invalid URL
# 48: Using currenturl to fetch the URL and (53:)checking it using assert
# 38 : marking for regression test

@pytest.mark.regression
def test_invalid_current_url_homepage(driver_method):

    driver = driver_method

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    url= driver.current_url

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    assert url == 'https://www.sauce_demo.com/'
