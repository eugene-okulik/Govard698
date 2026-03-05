from pages.base_page import BasePage
from pages.locators.product_page_office_locators import add_product_loc
from pages.locators.product_page_office_locators import product_name_loc
from pages.locators.product_page_office_locators import quantity_product
from pages.locators.product_page_office_locators import remove_product_loc


class ProductPageOffice(BasePage):
    page_url = "shop/furn-9999-office-design-software-7?category=9"

    def get_product_name_text(self):
        return self.find(product_name_loc).text_content()

    def check_product_name(self, expected_name):
        actual_name = self.get_product_name_text()
        assert (
            actual_name == expected_name
        ), f"Expected product name '{expected_name}', got '{actual_name}'"

    def add_product(self):
        self.find(add_product_loc).click()

    def remove_product(self):
        self.find(remove_product_loc).click()

    def wait_for_quantity(self, expected_value):
        return self.wait_for_value(quantity_product, expected_value)
