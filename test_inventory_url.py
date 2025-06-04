#Importing Packages

import pytest
from venv_web_page.Util.login_utils import LoginUtils

#positive-test case -> Login and fetch the dashboard URL
#importing login.utils 
#creating Object for class and accessing the method to log in the page
#driver_method is a function used to open the web page and use the URL
#using assert to check the expected with actual

@pytest.mark.sanity
def test_valid_current_inventory_url(driver_method):

    util=LoginUtils()
    util.verify_user_login(driver_method)

    driver=driver_method

    url = driver.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'


#Negative-test case -> fetching unexpected dashboard URL
#marked as a regression

@pytest.mark.regression
def test_invalid_current_url_inventory_page(driver_method):

    util = LoginUtils()
    util.verify_user_login(driver_method)

    driver = driver_method

    url= driver.current_url
    assert url=='https://www.saucedemo.com/'
