import requests


def all_request():
    response = requests.get(
        "http://objapi.course.qa-practice.com/object"
        ).json()
    assert response != {}, "response empty"


def new_obj():
    body = {
        "name": "test andriyanov",
        "data": {
            "group": 13121231,
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200
    response_api = response.json()["id"]
    return response_api


post_id = new_obj()


def obj_id():
    response = requests.get(
        f"http://objapi.course.qa-practice.com/object/{post_id}"
    ).json()
    assert response["id"] == post_id, "id not found"


def put_obj():
    body = {
        "name": "test andriyanovsssss",
        "data": {
            "group": "312312123asdasd",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{post_id}",
        json=body,
        headers=headers,
    )
    api_response = response.json()
    assert api_response["name"] == "test andriyanovsssss"
    assert response.status_code == 200


put_obj()


def patch_obj():
    body = {
        "name": "test andriyanovsssss121215",
        "data": {
            "group": "312312123asdasd",
        },
    }
    headers = {"Content-Type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{post_id}",
        json=body,
        headers=headers,
    )
    api_response = response.json()
    assert api_response["name"] == "test andriyanovsssss121215"
    assert response.status_code == 200


patch_obj()


def del_obj():
    headers = {"Content-Type": "application/json"}
    response = requests.delete(
        f"http://objapi.course.qa-practice.com/object/{post_id}",
        headers=headers,
    )
    assert response.status_code == 200


del_obj()
