from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

data: str = "ivan_test"


@pytest.fixture
def driver():
    chrome_driver: WebDriver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.get("https://www.qa-practice.com/elements/input/simple")
    yield chrome_driver
    chrome_driver.quit()


def test_input_field(driver: WebDriver):
    # Находим поле ввода
    input_field: WebElement = driver.find_element(By.ID, "id_text_string")

    # Вводим данные
    input_field.send_keys(data)

    # Нажимаем Enter
    input_field.send_keys(Keys.ENTER)

    # Ждём пока появится элемент с результатом (до 10 секунд)
    find_result: WebElement = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result-text"))
    )

    print("\nРезультат:", find_result.text)
    assert find_result.text == data
