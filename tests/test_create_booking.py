import pytest
from api.client_book import booking_base_client
from helpers.function import generate
from serializers.booking import Booking, BookingReduced
from resources.prepare import booking, data_for_parametrization_fields


@pytest.mark.parametrize('header', [{'application/xml'}, {'Content-Type'},
                                    {'Content-Type' 'application/json'}, {''},
                                    {'Content-Type': 'application/json'}])
def test_create_booking_parametrize_header(header):
    """ Проверка создания бронирования с корректным телом запроса и параметризованными данными заголовка запроса"""
    try:
        booking_parametrize_header = booking_base_client.create_booking(header, booking)
    except AttributeError:  # Перехват исключения при некорректных данных заголовка
        print(f'Incorrect header {header}, booking not created.')
    else:  # Создание и проверка бронирования с корректными данными заголовка
        assert Booking(**booking).dict() == Booking(**booking_parametrize_header.json()['booking']).dict()
        print(f'Correct header {header}, booking created.')


@pytest.mark.parametrize('data', data_for_parametrization_fields, ids=generate)
def test_create_booking_parametrize_body(data):
    """ Проверка создания бронирования с корректным заголовком запроса и параметризованными данными тела запроса"""
    header = {'Content-Type': 'application/json'}
    create_without_fields = booking_base_client.create_booking(header, data)
    if len(data) == 5:  # Создание и проверка бронирования без необязательного поля additionalneeds
        assert create_without_fields.status_code == 200
        assert BookingReduced(**data).dict() == BookingReduced(**create_without_fields.json()['booking']).dict()
    elif len(data) == 6:  # Создание и проверка бронирования с необязательным полем additionalneeds
        assert create_without_fields.status_code == 200
        assert Booking(**data).dict() == Booking(**create_without_fields.json()['booking']).dict()
    else:  # Количество полей в данных тела запроса меньше обязательного количества
        assert create_without_fields.status_code == 500
        assert str(type(create_without_fields.content)) == "<class 'bytes'>"
