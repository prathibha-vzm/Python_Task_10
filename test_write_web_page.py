#importing packages
#Importing LoginUtils to access the method

import pytest
from selenium.webdriver.common.by import By
from venv_web_page.Util.login_utils import LoginUtils


@pytest.mark.smoke
def test_extracting_text_from_webpage(driver_method):

    util = LoginUtils()
    util.verify_user_login(driver_method)

    driver = driver_method

    print(driver.title)

    print(driver.current_url)

    text= driver.find_element(By.TAG_NAME,'body').text

    with open("Webpage_task_11.txt",'w') as file:
        file.write(text)

# Question: 3 Fetch all the content from the webpage, Fetch Title, Fetch Current URL
# 12 & 13: Log in the page using verify_user_login method
# 21: Fetching the content using TAGNAME locator and text webelement
# 23: In with block Creating a Webpage_task_11.txt using open method
# 23: and setting it to write mode
# 24: writing the text to the file
# 9: marked as smoke - this check the flow from home to dashboard page.
