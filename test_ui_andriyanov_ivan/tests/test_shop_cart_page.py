import pytest


@pytest.mark.extended
def test_title(shop_cart_page):
    shop_cart_page.open_page()
    shop_cart_page.check_title("Shopping Cart | My Website")


@pytest.mark.extended
def test_header_shop_cart(shop_cart_page):
    shop_cart_page.open_page()
    shop_cart_page.check_header_text("Order overview")


@pytest.mark.extended
def test_basket_text(shop_cart_page):
    shop_cart_page.open_page()
    shop_cart_page.check_empty_cart_text("Your cart is empty!")
