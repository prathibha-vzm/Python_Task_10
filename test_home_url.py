import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.sanity
def test_valid_current_login_url(driver_method):

    driver = driver_method

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    url = driver.current_url
    assert url == 'https://www.saucedemo.com/'


    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    print("URL of this Page is ", url)

@pytest.mark.regression
def test_invalid_current_url_homepage(driver_method):

    driver = driver_method

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    url= driver.current_url
    assert url=='https://www.sauce_demo.com/'

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)