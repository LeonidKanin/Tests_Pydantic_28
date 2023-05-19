import pytest
from api.client_book import booking_base_client
from helpers.function import generate, path_params_prepare, list_data_of_response
from serializers.booking import BookingIdsResponse


@pytest.mark.parametrize('params', [{"firstname": "Jerry"}, {"lastname": "Tom"},
                                    {"firstname": "Jerry", "lastname": "Tom"}], ids=generate)
def test_get_booking_ids_parametrize_names_positive(create_booking, params):
    """Проверка получения id бронирований с параметризованными необязательными данными тела запроса
     и проверка структуры данных ответа"""

    booking_id, _ = create_booking  # Получение ключа авторизации созданного в фикстуре бронирования

    path_params = path_params_prepare(params)  # Сборка строки параметров пути запроса

    # Получение списка id бронирований с заданными параметрами
    get_ids = booking_base_client.get_booking_ids(path_params)

    list_id = list_data_of_response(get_ids)  # Создание списка id из данных ответа

    assert get_ids.status_code == 200
    assert str(type(get_ids.json())) == "<class 'list'>" and len(get_ids.json()) != 0
    assert booking_id in list_id  # Проверка, что в полученном списке находится id созданного запроса

    # Проверка соответствия структуры данных ответа из списка заданному классу
    for i in range(len(get_ids.json())):
        try:
            BookingIdsResponse(**get_ids.json()[i])
        except ValueError:
            print(f'Некорректные данные в ответе {get_ids.json()[i]}')


def test_get_booking_ids_without_params():
    """Проверка получения id бронирований и проверка структуры данных ответа"""

    get_ids = booking_base_client.get_booking_ids('')  # Получение списка id бронирований

    assert get_ids.status_code == 200
    assert str(type(get_ids.json())) == "<class 'list'>"
    if len(get_ids.json()) != 0:
        # Проверка соответствия структуры данных ответа из списка заданному классу
        for i in range(len(get_ids.json())):
            try:
                BookingIdsResponse(**get_ids.json()[i])
            except ValueError:
                print(f'Некорректные данные в ответе {get_ids.json()[i]}')
    else:
        # если спиcок питомцев пустой, то выкидываем исключение с текстом об отсутствии питомцев
        raise Exception('На сайте нет питомцев')
