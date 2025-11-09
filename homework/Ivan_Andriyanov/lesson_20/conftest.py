import pytest
import requests


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


# Фикстура, запускающаяся ОДИН РАЗ за всю сессию
@pytest.fixture(scope='session', autouse=True)
def hello():
    print("\n=== Start testing ===")
    yield
    print("=== Testing completed ===")


# Фикстура, запускающаяся ПЕРЕД и ПОСЛЕ каждого теста
@pytest.fixture(autouse=True)
def around_each_test():
    print("\n=== before test ===")
    yield
    print("=== after test ===")
