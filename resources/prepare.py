# Подготовка данных для тестирования и параметризации

from helpers.function import prepare_data_fields

sample = {
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

booking = {
    "firstname": "Jon",
    "lastname": "Red",
    "totalprice": 123,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2218-01-01",
        "checkout": "2219-01-01"
    },
    "additionalneeds": "Breakfast"
    }


data_for_parametrization_fields = prepare_data_fields(booking)
