from playwright.sync_api import Page, expect


def test_alert(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="Click").click()
    result = page.locator("#result-text")
    expect(result).to_have_text("Ok")


def test_active_tab(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    with page.context.expect_page() as new_page:
        page.get_by_role("link", name="Click").click()
    expect(new_page.value.locator("#result-text")).to_have_text(
        "I am a new page in a new tab"
    )


def test_wait_button(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    red_text_button = page.locator("#colorChange.text-danger")
    red_text_button.click()
