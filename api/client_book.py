import requests


class BookingBaseClient:

    url = "https://restful-booker.herokuapp.com"

    def post_api_key(self):
        # Получение ключа авторизации
        header = {'Content-Type': 'application/json'}
        data = {
            "username": "admin",
            "password": "password123"
        }
        res = requests.post(self.url + '/auth', headers=header, json=data)
        return res.json()['token']

    def create_booking(self, header, booking):
        # Создание бронирования
        return requests.post(self.url + '/booking', headers=header, json=booking)

    def get_booking_ids(self, params=None):
        # Получение id бронирований
        return requests.get(self.url + f'/booking' + params)

    def get_booking(self, booking_id):
        # Получение данных бронирования
        return requests.get(self.url + f'/booking/{booking_id}')

    def put_booking(self, booking_id, data, token):
        # Обновление бронирования
        header = {'Content-Type': 'application/json', 'Cookie': 'token=' + token}
        return requests.put(self.url + f'/booking/{booking_id}', headers=header, json=data)

    def patch_booking(self, booking_id, data, token):
        # Частичное обновление бронирования
        header = {'Content-Type': 'application/json', 'Cookie': 'token=' + token}
        return requests.patch(self.url + f'/booking/{booking_id}', headers=header, json=data)

    def delete_booking(self, booking_id, token):
        # Удаление бронирования
        header = {'Content-Type': 'application/json', 'Cookie': 'token=' + token}
        return requests.delete(self.url + f'/booking/{booking_id}', headers=header)

    def ping_booking(self):
        # Проверка, что API запущен
        return requests.get(self.url + '/ping')


booking_base_client = BookingBaseClient()
