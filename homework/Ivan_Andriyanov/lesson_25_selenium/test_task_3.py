from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_choose_language(driver):
    driver.get(url="https://www.qa-practice.com/elements/select/single_select")
    select_language = Select(driver.find_element(By.ID, "id_choose_language"))
    select_language.select_by_visible_text("Python")
    submit_click = driver.find_element(By.ID, "submit-id-submit")
    submit_click.click()
    result_modal = driver.find_element(By.ID, "result-text")
    assert result_modal.text == "Python"


def test_dynamically_load(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_click = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_click.click()

    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    assert result.text == "Hello World!"
