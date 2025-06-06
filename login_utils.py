#Importing Packages

import time
from selenium.webdriver.common.by import By

class LoginUtils:
    @staticmethod
    def verify_user_login(driver_method):
        driver = driver_method

        driver.find_element(By.NAME, "user-name").send_keys("standard_user")
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("secret_sauce")
        time.sleep(5)

        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)


# 8-18:  Under a class creating a method to log in the webpage - reusable purpose
# 14: Used CSS Selector to fetch the name locator for password element
