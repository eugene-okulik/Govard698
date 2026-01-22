from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия браузера."""
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver  # Возвращаем драйвер в тест
    chrome_driver.quit()  # После теста закрываем браузер


def test_new_tab(driver):

    # Открываем главную страницу магазина
    driver.get("http://testshop.qa-practice.com/")

    # 1. Находим ссылку на товар по тексту
    link = driver.find_element(By.LINK_TEXT, "Customizable Desk")

    # Ctrl+Click — открывает ссылку в новой вкладке
    # key_down(CONTROL) — зажимаем Ctrl
    # click(link) — кликаем по ссылке (пока Ctrl зажат)
    # key_up(CONTROL) — отпускаем Ctrl
    # perform() — выполняем всю цепочку действий
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(
        Keys.CONTROL
    ).perform()

    # 2. Переключаемся на новую вкладку
    # window_handles — список всех открытых вкладок [0] — первая, [1] — вторая
    driver.switch_to.window(driver.window_handles[1])

    # Проверяем что открылась правильная страница товара
    assert driver.find_element(By.TAG_NAME, "h1").text == "Customizable Desk"

    # 3. Добавляем товар в корзину
    # Кликаем по кнопке "Add to Cart"
    driver.find_element(By.ID, "add_to_cart").click()

    # Ждём появления модального окна и кликаем "Continue Shopping"
    # element_to_be_clickable — ждёт пока элемент станет видимым И кликабельным
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[span[text()='Continue Shopping']]")
        )
    )
    button.click()

    # ВАЖНО: Ждём пока сервер обработает запрос и товар добавится в корзину
    # Элемент my_cart_quantity имеет класс d-none когда корзина пуста
    # visibility_of_element_located ждёт пока d-none уберётся (элемент станет видимым)
    # Без этого ожидания мы можем закрыть вкладку до того как сервер ответит
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "my_cart_quantity"))
    )

    # 4. Закрываем вторую вкладку (с товаром)
    # close() — закрывает только текущую вкладку, не весь браузер
    driver.close()

    # 5. Возвращаемся на первую вкладку
    # После close() нужно переключиться, иначе Selenium потеряет фокус
    driver.switch_to.window(driver.window_handles[0])

    # Перезагружаем страницу чтобы получить актуальные данные с сервера
    # Первая вкладка не знает что товар добавлен — у неё старые данные в DOM
    driver.refresh()

    # Ждём пока после refresh корзина покажет товар
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "my_cart_quantity"))
    )

    # Кликаем по иконке корзины
    # CSS-селектор по атрибуту aria-label
    driver.find_element(By.CSS_SELECTOR, "a[aria-label='eCommerce cart']").click()

    # Ждём загрузки страницы корзины
    # Проверяем что появился заголовок "Order overview"
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[text()='Order overview']"))
    )

    # 6. Проверяем что в корзине именно тот товар который добавляли
    # XPath ищет элемент h6 с точным текстом названия товара
    product = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h6[text()='Customizable Desk (Steel, White)']")
        )
    )
    assert product.is_displayed()

    # 1. Открываем главную страницу магазина
    driver.get("http://testshop.qa-practice.com/")

    # 2. Находим картинку первого товара по атрибуту alt
    img = driver.find_element(By.CSS_SELECTOR, "img[alt='Customizable Desk']")

    # Наводим мышку на картинку
    # move_to_element() — перемещает курсор в центр элемента
    # perform() — выполняет действие
    # При наведении появляется кнопка корзины (hover-эффект)
    ActionChains(driver).move_to_element(img).perform()

    # 3. Ждём появления кнопки корзины и кликаем
    # element_to_be_clickable — ждёт пока элемент станет видимым И кликабельным
    # Кнопка появляется только при hover, поэтому нужно ожидание
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Shopping cart']"))
    ).click()

    # 4. Проверяем что товар появился в попапе корзины
    # visibility_of_element_located — ждёт пока элемент станет видимым
    # contains(text(), '...') — ищем элемент содержащий текст (не точное совпадение)
    # Используем contains потому что полный текст: "[FURN_0096] Customizable Desk (Steel, White)"
    element = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//td//strong[contains(text(), 'Customizable Desk')]")
        )
    )

    # Проверяем что элемент отображается
    # Технически избыточно (visibility_of_element_located уже это гарантирует)
    # Но делает тест более явным и читаемым
    assert element.is_displayed()
