from playwright.sync_api import expect

from saucedemo.src.pages.CartPage import CartPage
from saucedemo.src.pages.CheckoutYourInformationPage import CheckoutYourInformationPage
from saucedemo.src.pages.LoginPage import LoginPage


def test_place_order(setup_teardown) -> None:
    """
   Test for adding a product to the shopping cart
   """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()

    cart_p = CartPage(page)
    expect(cart_p._cart_header).to_have_text("Your Cart")
    expect(cart_p._inventory_item_price).to_have_text("$15.99")

    cart_p.take_screenshot('test_place_order.png')


def test_remove_item_from_cart(setup_teardown) -> None:
    """
   Test for removing a product from the shopping cart
   """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()

    cart_p = CartPage(page)
    cart_p.click_remove_item()

    expect(cart_p._cart_header).to_have_text("Your Cart")
    expect(products_p.cart_badge).not_to_be_visible()

    cart_p.take_screenshot('test_remove_item_from_cart.png')


def test_continue_shopping(setup_teardown) -> None:
    """
   Test for finishing the checkout process
   """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()

    cart_p = CartPage(page)
    cart_p.click_continue_shopping()

    expect(products_p.product_header).to_have_text('Products')

    products_p.take_screenshot('test_continue_shopping.png')


def test_checkout(setup_teardown) -> None:
    """
    Test for checking out your information
    """
    page = setup_teardown
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.click_add_to_cart()
    products_p.click_cart()
    cart_p = CartPage(page)
    cart_p.click_checkout()
    checkout_p = CheckoutYourInformationPage(page)

    expect(checkout_p.checkout_header()).to_have_text('Checkout: Your Information')

    checkout_p.take_screenshot('test_checkout.png')


