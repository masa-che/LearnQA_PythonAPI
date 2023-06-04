import requests
from Key_Frame_Classes.base_case import BaseCase
from Key_Frame_Classes.assertions import Assertions


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):           # метод получения данных не авторизованного пользователя
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        print(response.content)                         # b'{"username":"Vitaliy"}'  возвращаемые данных запроса get

        Assertions.assert_json_has_key(response, "username")   # проверка на содержание в ответе - "username"
        Assertions.assert_json_has_not_key(response, "email")  # проверки на отсутствие в ответе полей с именами email, firstName, lastName
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    # python -m pytest -s tests/test_user_get.py -k test_get_user_details_not_auth  (запуск одного этого метода)

    def test_get_user_details_auth_as_same_user(self):  # метод проверки авторизованного пользователя (один и тот же пользователь)
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        # запрос на авторизацию
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        # вытаскиваем значения из json (при помощи функций из base_case)
        auth_sid = self.get_cookie(response1, 'auth_sid')
        token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, 'user_id')

        # после авторизации, вторым запросом get, проверяем наличие всех необходимых ключей в теле ответа json (Assert)
        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    # python -m pytest -s tests/test_user_get.py -k test_get_user_details_auth_as_same_user
