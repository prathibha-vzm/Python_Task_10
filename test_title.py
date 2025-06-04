#Importing Packages 
# Importing LoginUtils to access the method from the class
import time
import pytest
from selenium.webdriver.common.by import By
from venv_web_page.Util.login_utils import LoginUtils

#Positive - test case -> Fetch the title from the web page
# 22: Fetching the title using title and storing it in a variable 
# 30: checking the actual result using assert

@pytest.mark.sanity
def test_valid_title_page(driver_method):

    driver=driver_method

    driver.find_element(By.NAME, "user-name").send_keys("standard_user")
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys("secret_sauce")

    title = driver.title


    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    print("Title", title)

    assert title == 'Swag Labs'


#Negative - test case -> Fetch the title from the web page 
# 41 & 42 Used the LoginUtils to reduce the line of coding to Login the webpage
# 46: Fetching the title using title and storing it in a variable 
# 50: checking the actual result using assert with invalid title 

@pytest.mark.regression
def test_invalid_title_page(driver_method):

    util = LoginUtils()
    util.verify_user_login(driver_method)

    driver = driver_method

    title= driver.title

    print("Title",driver.title)

    assert title == 'Swag'
