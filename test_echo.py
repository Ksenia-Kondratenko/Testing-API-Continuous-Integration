import requests
import pytest

BASE_URL = "https://postman-echo.com/"

# Тест 1: Проверка GET-запроса с параметрами
def test_get_request_with_parameters():
    params = {"name": "123", "password": "onetwothree"}
    response = requests.get(BASE_URL + "get", params=params)

    # Проверка статуса ответа
    assert response.status_code == 400

    # Проверка присутствия переданных параметров в ответе
    assert response.json()["args"] == params


# Тест 2: Проверка POST-запроса с JSON-телом
def test_post_request_with_json():
    data = {
        "name": "test",
        "password": "5555abc",
        "email": "post4@qqq.com"
    }
    response = requests.post(BASE_URL + "post", json=data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка соответствия принятого и возвращённого JSON
    assert response.json()["json"] == data


# Тест 3: Проверка PUT-запроса с JSON-телом
def test_put_request_with_json():
    data = {
        "name": "test111",
        "password": "threetwoone",
        "email": "cat111@gmail.com"
    }
    response = requests.put(BASE_URL + "put", json=data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка соответствия принятого и возвращённого JSON
    assert response.json()["json"] == data


# Тест 4: Проверка DELETE-запроса с параметром
def test_delete_request_with_parameter():
    params = {"id": "44555666"}
    response = requests.delete(BASE_URL + "delete", params=params)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка присутствия переданного параметра в ответе
    assert response.json()["args"]["id"] == params["id"]


# Тест 5: Проверка PATCH-запроса с JSON-телом
def test_patch_request_with_json():
    data = {
        "email": "anyemail@mail.com"
    }
    response = requests.patch(BASE_URL + "patch", json=data)

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка соответствия принятого и возвращённого JSON
    assert response.json()["json"] == data