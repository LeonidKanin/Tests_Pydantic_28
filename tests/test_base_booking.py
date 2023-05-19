from api.client_book import booking_base_client
from serializers.booking import Booking
from resources.prepare import booking


def test_ping_booking():
    """Проверка, что API запущен"""

    ping = booking_base_client.ping_booking()

    assert ping.status_code == 201, 'API не запущен'
    assert ping.text == 'Created'


def test_create_and_get_booking():
    """Создание бронирования, получение данных созданного бронирования и сравнение с начальными данными"""

    # Создание бронирования и получение его id
    header = {'Content-Type': 'application/json'}
    create_booking = booking_base_client.create_booking(header, booking)
    booking_id = create_booking.json()['bookingid']

    # Получение данных созданного бронирования
    get_booking = booking_base_client.get_booking(booking_id)

    # Сравнение данных созданного бронирования с начальными данными
    assert Booking(**booking).dict() == Booking(**get_booking.json()).dict()

    assert get_booking.status_code == 200
    assert str(type(get_booking.json())) == "<class 'dict'>"


def test_delete_booking(create_booking):
    """Проверка удаления созданного бронирования"""

    # Создание бронирования
    booking_id, token = create_booking

    # Удаление бронирования
    delete_booking = booking_base_client.delete_booking(booking_id, token)

    assert delete_booking.status_code == 201
    assert delete_booking.text == 'Created'

    # Попытка удаления несуществующего бронирования
    delete_booking_more = booking_base_client.delete_booking(booking_id, token)

    assert delete_booking_more.status_code == 405
    assert delete_booking_more.text == 'Method Not Allowed'
