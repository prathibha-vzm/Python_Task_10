import pytest
from selenium import webdriver

# Using fixture to preapre the test environment (to open the browser and use it)
# reusable purpose

@pytest.fixture
def driver_method():

    driver=webdriver.Chrome()
    
    driver.get("https://www.saucedemo.com/")
    
    return driver
