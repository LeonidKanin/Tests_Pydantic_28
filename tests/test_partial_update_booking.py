import pytest
from api.client_book import booking_base_client
from helpers.function import generate
from resources.prepare import sample, booking, data_for_parametrization_fields
from serializers.booking import Booking


@pytest.mark.parametrize('data', data_for_parametrization_fields, ids=generate)
def test_partial_update_parametrize_body(create_booking, data):
    """Частичное и полное обновление бронирования с параметризованными необязательными полями данных тела запроса"""

    booking_id, token = create_booking  # Получение id и ключа авторизации созданного в фикстуре бронирования

    partial_update = booking_base_client.patch_booking(booking_id, data, token)

    # Проверка, что бронирование успешно обновляется с любым
    # (от 0 до 6) количеством необязательных полей данных тела запроса
    assert partial_update.status_code == 200
    assert str(type(partial_update.content)) == "<class 'bytes'>"
    if len(data) == 0:  # Проверка, что при попытке обновления без данных, бронирование не меняется
        assert str(type(partial_update.json())) == "<class 'dict'>"
        assert Booking(**sample).dict() == Booking(**partial_update.json()).dict()
    elif len(data) == 6:  # Проверка успешности полного обновления данных бронирования
        assert str(type(partial_update.json())) == "<class 'dict'>"
        assert Booking(**booking).dict() == Booking(**partial_update.json()).dict()
    else:  # Проверка успешности частичного обновления данных бронирования
        assert partial_update.status_code == 200
        assert str(type(partial_update.json())) == "<class 'dict'>"
