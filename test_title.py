import time

import pytest
from selenium.webdriver.common.by import By

from venv_web_page.Util.login_utils import LoginUtils

@pytest.mark.sanity
def test_valid_title_page(driver_method):

    driver=driver_method

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    title = driver.title
    assert title == 'Swag Labs'

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    print("Title", title)

@pytest.mark.regression
def test_invalid_title_page(driver_method):

    util = LoginUtils()
    util.verify_user_login(driver_method)

    driver = driver_method

    title= driver.title
    assert title == 'Swag'
    print("Title",driver.title)