import time

import pytest
from selenium.webdriver.common.by import By

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

@pytest.mark.regression
def test_invalid_login_page(driver_method):

    driver=driver_method

    user_name=driver.find_element(By.NAME,"user-name").send_keys("standard_user")
    time.sleep(2)
    assert user_name=='standard_user'

    password= driver.find_element(By.NAME,"password").send_keys("sauce")
    assert password=='secret_sauce'

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)