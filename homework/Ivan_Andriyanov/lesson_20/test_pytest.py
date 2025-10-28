import requests
import pytest


# Фикстура, запускающаяся ПЕРЕД и ПОСЛЕ каждого теста
@pytest.fixture(autouse=True)
def around_each_test():
    print("\n=== before test ===")
    yield
    print("=== after test ===")


# Фикстура, запускающаяся ОДИН РАЗ за всю сессию
@pytest.fixture(scope='session', autouse=True)
def hello():
    print("\n=== Start testing ===")
    yield
    print("=== Testing completed ===")


# Фикстура, создающая и удаляющая объект для каждого теста
@pytest.fixture()
def created_object():
    body = {
        "name": "ivanka",
        "data": {"group": 13121231},
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200
    post_id = response.json()["id"]
    print(f"Created post id: {post_id}")

    yield post_id

    print(f"Deleting post {post_id}")
    requests.delete(f"http://objapi.course.qa-practice.com/object/{post_id}")


# 🔹 Тест на создание — параметризованный (создаёт 3 разных объекта)
@pytest.mark.parametrize('name', ['mashka', 'kakashka', 'martushka'])
def test_create_object(name):
    body = {
        "name": name,
        "data": {"group": 13121231},
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body,
        headers=headers,
    )

    assert response.status_code == 200
    api_response = response.json()
    print(f"Created: {api_response}")
    assert api_response["name"] == name

    # Чистим за собой
    requests.delete(f"http://objapi.course.qa-practice.com/object/{api_response['id']}")


# 🔹 Тест на получение по id
def test_get_post(created_object):
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{created_object}")
    assert response.status_code == 200
    api_response = response.json()
    print(f"Get object id={api_response['id']}")
    assert api_response["id"] == created_object, "ID not found"


# 🔹 Тест на изменение (помечен как medium)
@pytest.mark.medium
def test_put_post(created_object):
    body = {
        "name": "andriyanov ivan",
        "data": {"group": "password test"},
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{created_object}",
        json=body,
        headers=headers,
    )

    assert response.status_code == 200
    api_response = response.json()
    print(f"Updated object: {api_response}")
    assert api_response["name"] == "andriyanov ivan"


# 🔹 Тест на частичное изменение (помечен как critical)
@pytest.mark.parametrize('name', ['alisa', 'lesha', 'luda'])
@pytest.mark.critical
def test_patch_post(created_object, name):
    body = {
        "name": name,
        "data": {"group": "312312123asdasd"},
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{created_object}",
        json=body,
        headers=headers,
    )

    assert response.status_code == 200
    api_response = response.json()
    print(f"Имя обновилось на: {api_response['name']}")
    assert api_response["name"] == name, "name not found"


def test_del_obj(created_object):
    headers = {"Content-Type": "application/json"}
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{created_object}",
        headers=headers,
    )
    assert response.status_code == 200
