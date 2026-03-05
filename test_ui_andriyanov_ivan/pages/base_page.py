from playwright.sync_api import Page, Locator, expect


class BasePage:
    base_url = "http://testshop.qa-practice.com/"
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url is not None:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def hover(self, locator: str) -> Locator:
        element = self.find(locator)
        element.hover()
        return element

    def wait_for_element(self, locator: str, timeout=10000) -> Locator:
        element = self.find(locator)
        element.wait_for(timeout=timeout, state="visible")
        return element

    def send_text(self, locator: str, text: str) -> Locator:
        element = self.find(locator)
        element.fill(text)
        return element

    def check_title(self, text: str):
        assert self.page.title() == text

    def wait_for_value(self, locator: str, expected_value: str, timeout=10000) -> Locator:
        element = self.find(locator)
        expect(element).to_have_value(expected_value, timeout=timeout)
        return element
