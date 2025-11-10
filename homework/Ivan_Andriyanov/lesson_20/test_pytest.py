import requests
import pytest
import allure


# 🔹 Тест на создание — параметризованный (создаёт 3 разных объекта)
@allure.feature('Many posts')
@allure.story('Создаем 3 логина')
@pytest.mark.parametrize('name', ['mashka', 'kakashka', 'martushka'])
def test_create_object(name):
    with allure.step("Формируем тело запроса для создания поста"):
        body = {"name": name, "data": {"group": 13121231}}
        headers = {"Content-Type": "application/json"}

    with allure.step("Отправляем POST-запрос на создание объекта"):
        response = requests.post(
            "http://objapi.course.qa-practice.com/object",
            json=body,
            headers=headers,
        )

    with allure.step("Проверяем, что ответ успешный (200 OK)"):
        assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    with allure.step("Проверяем корректность данных в ответе"):
        api_response = response.json()
        allure.attach(str(api_response), name="API response", attachment_type=allure.attachment_type.TEXT)
        assert api_response["name"] == name

    with allure.step("Удаляем созданный объект (cleanup)"):
        requests.delete(f"http://objapi.course.qa-practice.com/object/{api_response['id']}")


# 🔹 Тест на получение по id
@allure.feature('Posts')
@allure.story('Получаем ID поста')
def test_get_post(created_object):
    with allure.step(f"Отправляем GET-запрос на получение объекта {created_object}"):
        response = requests.get(f"http://objapi.course.qa-practice.com/object/{created_object}")

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200, f"Unexpected status: {response.status_code}"

    with allure.step("Проверяем ID объекта в ответе"):
        api_response = response.json()
        allure.attach(str(api_response), name="API response", attachment_type=allure.attachment_type.TEXT)
        assert api_response["id"] == created_object, "ID not found"


# 🔹 Тест на изменение (помечен как medium)
@allure.feature('Posts')
@allure.story('Изменяем пост полностью')
@pytest.mark.medium
def test_put_post(created_object):
    with allure.step("Готовим тело запроса для полного обновления поста"):
        body = {"name": "andriyanov ivan", "data": {"group": "password test"}}
        headers = {"Content-Type": "application/json"}

    with allure.step(f"Отправляем PUT-запрос для объекта {created_object}"):
        response = requests.put(
            f"http://objapi.course.qa-practice.com/object/{created_object}",
            json=body,
            headers=headers,
        )

    with allure.step("Проверяем статус-код и тело ответа"):
        assert response.status_code == 200
        api_response = response.json()
        allure.attach(str(api_response), name="Updated object", attachment_type=allure.attachment_type.TEXT)
        assert api_response["name"] == "andriyanov ivan"


# 🔹 Тест на частичное изменение (помечен как critical)
@allure.feature('Posts')
@allure.story('Изменяем пост частично')
@pytest.mark.parametrize('name', ['alisa', 'lesha', 'luda'])
@pytest.mark.critical
def test_patch_post(created_object, name):
    with allure.step("Формируем тело PATCH-запроса"):
        body = {"name": name, "data": {"group": "312312123asdasd"}}
        headers = {"Content-Type": "application/json"}

    with allure.step(f"Отправляем PATCH-запрос для объекта {created_object}"):
        response = requests.patch(
            f"http://objapi.course.qa-practice.com/object/{created_object}",
            json=body,
            headers=headers,
        )

    with allure.step("Проверяем успешность обновления и имя в ответе"):
        assert response.status_code == 200
        api_response = response.json()
        allure.attach(str(api_response), name=f"Updated name: {name}", attachment_type=allure.attachment_type.TEXT)
        assert api_response["name"] == name, "name not found"


# 🔹 Тест на удаление
@allure.feature('Posts')
@allure.story('Удаляем пост')
@allure.title('Удаление поста по ID и проверка успешного статуса')
def test_del_obj(created_object):
    with allure.step(f"Отправляем DELETE-запрос для объекта {created_object}"):
        headers = {"Content-Type": "application/json"}
        response = requests.delete(
            f"http://objapi.course.qa-practice.com/object/{created_object}",
            headers=headers,
        )
        allure.attach(
            f"Status code: {response.status_code}\nResponse text: {response.text}",
            name="DELETE response",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверяем, что объект успешно удален (200 OK)"):
        assert response.status_code == 201, f"Unexpected status: {response.status_code}"
