import pytest
from api.client_book import booking_base_client

@pytest.fixture(scope='session')
def create_booking():
    """Предварительное создание бронирования и получение id и ключа авторизации"""

    data = {
    "firstname": "Jerry",
    "lastname": "Tom",
    "totalprice": 321,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "3118-01-01",
        "checkout": "3119-01-01"
    },
    "additionalneeds": "All inclusive"
    }
    header = {'Content-Type': 'application/json'}

    create_booking = booking_base_client.create_booking(header, data)

    booking_id = create_booking.json()['bookingid']
    token = booking_base_client.post_api_key()

    return booking_id, token
