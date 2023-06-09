from playwright.sync_api import Page, expect

from saucedemo.src.pages.LoginPage import LoginPage


def test_login_with_standard_user(setup_teardown) -> None:
    """
    Tests logging in with a valid username and password.
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    expect(products_p.product_header).to_be_visible()
    expect(products_p.product_header).to_have_text('Products')

    login_p.take_screenshot('test_login_with_standard_user.png')


def test_login_with_invalid_user(setup_teardown) -> None:
    """
    Tests logging in with an invalid username and password.
    """

    page = setup_teardown
    credentials = {'username': 'nonstandard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    login_p.do_login(credentials)
    expected_fail_massage = 'Username and password do not match any user in this service'
    expect(login_p.error_msg_locator).to_contain_text(expected_fail_massage)

    login_p.take_screenshot('test_login_with_invalid_user.png')


def test_login_no_user_name(setup_teardown) -> None:
    """
    Tests logging in without a username.
    """
    page = setup_teardown
    login_p = LoginPage(page)
    login_p.click_login()
    expected_fail_massage = 'Username is required'
    expect(login_p.error_msg_locator).to_contain_text(expected_fail_massage)

    login_p.take_screenshot('test_login_no_user_name.png')


def test_login_no_password(setup_teardown) -> None:
    """
    Tests logging in without a password.
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': ''}
    login_p = LoginPage(page)
    login_p.do_login(credentials)

    expected_fail_massage = 'Password is required'
    expect(login_p.error_message_password).to_contain_text(expected_fail_massage)

    login_p.take_screenshot('test_login_no_password.png')


def test_access_inventory_without_login(setup_teardown) -> None:
    """
    Tests accessing the inventory page without logging in.
    """
    page = setup_teardown
    page.goto('https://www.saucedemo.com/inventory.html')
    login_p = LoginPage(page)
    expect(login_p.error_msg_locator).to_contain_text("You can only access '/inventory.html' when you are logged in.")
    login_p.take_screenshot('test_access_inventory_without_login.png')
