# Вспомогательные функции

def prepare_data_fields(booking):
    # Создание массива для параметризации данных тела запроса
    data = [booking]
    for i in range(0, len(booking)):
        change = booking.copy()
        for j in range(0, i + 1):
            change.popitem()
        data.append(change)
    data.reverse()
    return data


def generate(val):
    # Генерирование названий для параметризации
    return f'{val}'


def path_params_prepare(data):
    # Сборка строки параметров пути запроса
    str_params = "?"
    for key, value in data.items():
        str_params = str_params + f'{key}={value}&'
    str_params = str_params[:-1]
    return str_params


def list_data_of_response(data):
    # Создание списка id из данных ответа
    list_data = []
    for i in range(len(data.json())):
        list_data.append(data.json()[i]['bookingid'])
    return list_data
