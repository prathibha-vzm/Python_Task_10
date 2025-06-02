import pytest

from venv_web_page.Util.login_utils import LoginUtils

@pytest.mark.sanity
def test_valid_current_inventory_url(driver_method):

    util=LoginUtils()
    util.verify_user_login(driver_method)

    driver=driver_method

    url = driver.current_url
    assert url == 'https://www.saucedemo.com/inventory.html'


@pytest.mark.regression
def test_invalid_current_url_inventory_page(driver_method):

    util = LoginUtils()
    util.verify_user_login(driver_method)

    driver = driver_method

    url= driver.current_url
    assert url=='https://www.saucedemo.com/'