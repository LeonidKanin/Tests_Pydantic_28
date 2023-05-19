import pytest
import requests
from helpers.function import generate
from serializers.booking import AuthBody, AuthResponse


@pytest.mark.parametrize('request_body', [{''}, {"username": "admin"}, {"password": "password123"},
                                          {"username": "", "password": "password123"},
                                          {"username": "admin", "password": ""},
                                          {"username": "123", "password": 123},
                                          {"username": "admin", "password": "password123"}],
                         ids=generate)
def test_auth_parametrize_request_body(request_body):
    """ Тест получения ключа авторизации с параметризованными данными тела запроса"""

    url = "https://restful-booker.herokuapp.com"
    header = {'Content-Type': 'application/json'}

    try:
        AuthBody(**request_body)  # Проверка соответствия данных в теле запроса требованиям заданного класса
    except ValueError:
        print(f'Некорректные данные {request_body} в теле запроса')
    except TypeError:
        print(f'Некорректные данные {request_body} в теле запроса')
    else:  # Если данные в теле запроса соответствуют требованиям класса, делаем запрос
        booking_auth = requests.post(url + '/auth', headers=header, json=request_body)
        assert booking_auth.status_code == 200
        try:
            AuthResponse(**booking_auth.json())  # Проверяем данные в ответе требованиям заданного класса
        except ValueError:
            print(f'Несуществующие учетные данные, {booking_auth.json()}')
        else:
            print(f'Ключ авторизации получен, {booking_auth.json()}')
