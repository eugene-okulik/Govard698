from playwright.sync_api import BrowserContext
import pytest
from pages.shop_cart_page import ShopCartPage
from pages.shop_cart_desk_page import ShopCartPageDesk
from pages.product_page_office import ProductPageOffice


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def shop_cart_page(page):
    return ShopCartPage(page)


@pytest.fixture()
def shop_cart_page_desk(page):
    return ShopCartPageDesk(page)


@pytest.fixture()
def product_page_office(page):
    return ProductPageOffice(page)
