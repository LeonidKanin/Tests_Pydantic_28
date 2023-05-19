import pytest
from api.client_book import booking_base_client
from helpers.function import generate
from resources.prepare import booking, data_for_parametrization_fields
from serializers.booking import Booking


@pytest.mark.parametrize('data', data_for_parametrization_fields, ids=generate)
def test_update_parametrize_body(create_booking, data):

    booking_id, token = create_booking  # Получение id и ключа авторизации созданного в фикстуре бронирования

    update_booking = booking_base_client.put_booking(booking_id, data, token)

    if len(data) == 5:  # Проверка обновления бронирования без необязательного поля additionalneeds
        assert update_booking.status_code == 200
        assert str(type(update_booking.json())) == "<class 'dict'>"
    elif len(data) == 6:  # Проверка обновления бронирования c необязательным полем additionalneeds
        assert update_booking.status_code == 200
        assert Booking(**booking).dict() == Booking(**update_booking.json()).dict()
    else:  # Проверка невозможности частичного обновления данных бронирования
        assert update_booking.status_code == 400
        assert str(type(update_booking.content)) == "<class 'bytes'>"
