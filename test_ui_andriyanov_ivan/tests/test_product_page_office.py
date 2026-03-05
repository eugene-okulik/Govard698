import pytest


@pytest.mark.extended
def test_check_product_name(product_page_office):
    product_page_office.open_page()
    product_page_office.check_product_name("Office Design Software")


def test_add_product(product_page_office):
    product_page_office.open_page()
    product_page_office.add_product()
    product_page_office.wait_for_quantity("2")


def test_remove_product(product_page_office):
    product_page_office.open_page()
    product_page_office.remove_product()
    product_page_office.wait_for_quantity("1")
