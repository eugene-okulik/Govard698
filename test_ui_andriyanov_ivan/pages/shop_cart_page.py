from pages.base_page import BasePage
from pages.locators.shop_cart_locators import basket_empty_text_loc
from pages.locators.shop_cart_locators import header_shop_cart_loc


class ShopCartPage(BasePage):
    page_url = "shop/cart"

    def get_header_text(self):
        return self.find(header_shop_cart_loc).text_content()

    def check_header_text(self, expected_text):
        actual_text = self.get_header_text()
        assert (
            actual_text == expected_text
        ), f"Expected header '{expected_text}', got '{actual_text}'"

    def get_empty_cart_text(self):
        return self.find(basket_empty_text_loc).text_content().strip()

    def check_empty_cart_text(self, expected_text):
        actual_text = self.get_empty_cart_text()
        assert (
            actual_text == expected_text
        ), f"Expected empty cart text '{expected_text}', got '{actual_text}'"
