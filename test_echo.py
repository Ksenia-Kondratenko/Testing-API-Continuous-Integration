import requests
import pytest

BASE_URL = "https://postman-echo.com/"

# Фикстура для подготовки общих параметров
@pytest.fixture
def common_params():
    return {"name": "123", "password": "onetwothree"}

# Фикстура для подготовки общего JSON-тела
@pytest.fixture
def common_data():
    return {
        "name": "test",
        "password": "5555abc",
        "email": "post4@qqq.com"
    }

# Тест 1: Проверка GET-запроса с параметрами
def test_get_request_with_parameters(common_params):
    response = requests.get(BASE_URL + "get", params=common_params)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка присутствия переданных параметров в ответе
    assert response.json()["args"] == common_params


# Тест 2: Проверка POST-запроса с JSON-телом
def test_post_request_with_json(common_data):
    response = requests.post(BASE_URL + "post", json=common_data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка соответствия принятого и возвращённого JSON
    assert response.json()["json"] == common_data


# Тест 3: Проверка PUT-запроса с JSON-телом
def test_put_request_with_json(common_data):
    put_data = {
        "name": "test111",
        "password": "threetwoone",
        "email": "cat111@gmail.com"
    }
    response = requests.put(BASE_URL + "put", json=put_data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка соответствия принятого и возвращённого JSON
    assert response.json()["json"] == put_data


# Тест 4: Проверка DELETE-запроса с параметром
def test_delete_request_with_parameter():
    delete_params = {"id": "44555666"}
    response = requests.delete(BASE_URL + "delete", params=delete_params)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка присутствия переданного параметра в ответе
    assert response.json()["args"]["id"] == delete_params["id"]


# Тест 5: Проверка PATCH-запроса с JSON-телом
def test_patch_request_with_json():
    patch_data = {
        "email": "anyemail@mail.com"
    }
    response = requests.patch(BASE_URL + "patch", json=patch_data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка соответствия принятого и возвращённого JSON
    assert response.json()["json"] == patch_data