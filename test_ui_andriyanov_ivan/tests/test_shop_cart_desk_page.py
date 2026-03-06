import pytest


@pytest.mark.extended
def test_click_on_basket(shop_cart_page_desk):
    shop_cart_page_desk.open_page()
    shop_cart_page_desk.click_basket()
    shop_cart_page_desk.check_header_modal_text("Add to cart")


@pytest.mark.extended
def test_find_two_img(shop_cart_page_desk):
    shop_cart_page_desk.open_page()
    shop_cart_page_desk.check_second_product_displayed()


@pytest.mark.extended
def test_write_to_search_input(shop_cart_page_desk):
    shop_cart_page_desk.open_page()
    shop_cart_page_desk.fill_search_input("test_text")
    shop_cart_page_desk.check_search_input_value("test_text")
