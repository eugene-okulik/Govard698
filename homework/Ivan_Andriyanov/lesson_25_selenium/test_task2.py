from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Тестовые данные
TEST_DATA = {
    "first_name": "Ivan",
    "last_name": "Andriianov",
    "email": "test@mail.ru",
    "gender": "Male",
    "mobile": "9959959595",
    "birth_year": "1995",
    "birth_month": "November",
    "birth_day": "015",
    "subject": "Maths",
    "hobby": "Sports",
    "address": "Moscow, Red Square 1",
    "state": "NCR",
    "city": "Delhi",
}


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get("https://demoqa.com/automation-practice-form")
    yield chrome_driver
    chrome_driver.quit()


def test_fill_form(driver):
    # Name
    driver.find_element(By.ID, "firstName").send_keys(TEST_DATA["first_name"])
    driver.find_element(By.ID, "lastName").send_keys(TEST_DATA["last_name"])

    # Email
    driver.find_element(By.ID, "userEmail").send_keys(TEST_DATA["email"])

    # Gender
    driver.find_element(By.XPATH, f"//label[text()='{TEST_DATA['gender']}']").click()

    # Mobile
    driver.find_element(By.ID, "userNumber").send_keys(TEST_DATA["mobile"])

    # Date of Birth
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys(
        TEST_DATA["birth_year"]
    )
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys(
        TEST_DATA["birth_month"]
    )
    driver.find_element(
        By.CSS_SELECTOR, f".react-datepicker__day--{TEST_DATA['birth_day']}"
    ).click()

    # Subjects
    subject_input = driver.find_element(By.ID, "subjectsInput")
    subject_input.send_keys(TEST_DATA["subject"])
    subject_input.send_keys(Keys.ENTER)

    # Hobbies
    driver.find_element(By.XPATH, f"//label[text()='{TEST_DATA['hobby']}']").click()

    # Current Address
    driver.find_element(By.ID, "currentAddress").send_keys(TEST_DATA["address"])

    # State
    driver.find_element(By.ID, "state").click()
    driver.find_element(By.XPATH, f"//div[text()='{TEST_DATA['state']}']").click()

    # City
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.XPATH, f"//div[text()='{TEST_DATA['city']}']").click()

    # Submit
    driver.find_element(By.ID, "submit").click()

    # Проверка что форма отправилась
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )
    assert "Thanks for submitting the form" in modal.text

    # Вывод результата
    print("\n" + modal.text)
