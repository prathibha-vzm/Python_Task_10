#Importing packages

import time
import pytest
from selenium.webdriver.common.by import By


# Positive Test case -> Valid Login Credentials
# Using Name locator to input username and password
# Using ID locator to click the web element
# Using "assert" for URL to check the successful login


@pytest.mark.sanity
def test_valid_login_page(driver_method):

    driver=driver_method

    driver.find_element(By.NAME,"user-name").send_keys("standard_user")
    time.sleep(2)


    driver.find_element(By.NAME,"password").send_keys("secret_sauce")

    driver.find_element(By.ID,"login-button").click()
    time.sleep(2)

    url=driver.current_url
    assert url=='https://www.saucedemo.com/inventory.html'


#Marking the test as regression 
# Negative Test case -> Invalid Login Credentials
# Using Name locator to input valid username and Invalid password
# Using ID locator to click the (Login) web element
# Using assert to check the expected with actual output

@pytest.mark.regression
def test_invalid_login_page(driver_method):

    driver=driver_method

    driver.find_element(By.NAME,"user-name").send_keys("standard_user")
    time.sleep(2)


    password= driver.find_element(By.NAME,"password").send_keys("sauce")


    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    assert password == 'secret_sauce'
