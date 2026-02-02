from playwright.sync_api import Page, expect
from time import sleep


def test_fill_form(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    user_name = page.get_by_role("textbox", name="username")
    user_name.fill("test_ivan")
    sleep(1)
    password = page.get_by_role("textbox", name="password")
    password.fill("123456")
    page.get_by_role("button", name="Login").click()
    sleep(3)


def test_fill_form_two(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    first_name = page.get_by_role("textbox", name="First Name")
    first_name.fill("Ivan")
    last_name = page.get_by_role("textbox", name="Last Name")
    last_name.fill("Andriyanov")
    email = page.locator("#userEmail")
    email.fill("mail12345234@mail.ru")
    page.locator('//label[@for="gender-radio-1"]').click()
    mobile_number = page.locator('//input[@placeholder="Mobile Number"]')
    mobile_number.fill("1234567891")
    date_birth = page.locator("#dateOfBirthInput")
    date_birth.fill("14 Feb 1995")
    date_birth.press("Enter")
    subjects = page.locator("#subjectsInput")
    subjects.fill("Maths")
    page.wait_for_selector(".subjects-auto-complete__option")
    subjects.press("Enter")
    page.locator('//label[@for="hobbies-checkbox-1"]').click()
    adress = page.locator('//textarea[@placeholder="Current Address"]')
    adress.fill("moskow")
    select_state = page.locator("#react-select-3-input")
    select_state.fill("NCR")
    page.wait_for_selector('div[id*="react-select"][class*="option"]')
    select_state.press("Enter")

    select_city = page.locator("#react-select-4-input")
    select_city.fill("Delhi")
    page.wait_for_selector('div[id*="react-select"][class*="option"]')
    select_city.press("Enter")
    page.locator("#submit").click()
    sleep(5)
