import pytest
from selenium import webdriver
@pytest.fixture
def driver_method():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver
