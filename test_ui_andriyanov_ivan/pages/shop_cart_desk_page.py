from pages.base_page import BasePage
from pages.locators.desk_page_locators import DeskPageLocators as L


class ShopCartPageDesk(BasePage):
    page_url = "shop/category/desks-1"

    def click_basket(self):
        self.hover(L.button_basket_loc)
        self.find(L.button_basket_loc).click()

    def header_modal(self):
        return self.wait_for_element(L.modal_header_loc)

    def get_header_modal_text(self):
        return self.header_modal().text_content()

    def check_header_modal_text(self, expected_text):
        actual_text = self.get_header_modal_text()
        assert (
            actual_text == expected_text
        ), f"Expected modal header '{expected_text}', got '{actual_text}'"

    def is_second_product_displayed(self):
        return self.find(L.product_img_two_loc).is_visible()

    def check_second_product_displayed(self):
        assert self.is_second_product_displayed(), "Second product image is not displayed"

    def fill_search_input(self, text):
        search_input = self.wait_for_element(L.search_input_loc)
        search_input.fill(text)
        return search_input

    def check_search_input_value(self, expected_text):
        actual_text = self.find(L.search_input_loc).input_value()
        assert (
            actual_text == expected_text
        ), f"Expected search input value '{expected_text}', got '{actual_text}'"
