import requests
import pytest

from Key_Frame_Classes.base_case import BaseCase
from Key_Frame_Classes.assertions import Assertions


class TestAuth(BaseCase):
    # по сравнению с предыдущим заданием, здесь используется list а не dict
    exclude_params = [    # параметры для негативного теста с куки и токеном
        "no_cookie",      # в тесте будет либо куки, либо токен
        "no_token"        # без которых user_id пользователя должен == 0
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_auth_user(self):
        url = "https://playground.learnqa.ru/api/user/auth"
        response2 = requests.get(url, headers={"x-csrf-token": self.token}, cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(response2, "user_id", self.user_id_from_auth_method, "User id auth method isn't equal to usrt id from check method")

    # негативная проверка на авторизацию

    @pytest.mark.parametrize('condition', exclude_params)  # подключаем в виде параметра exclude_params и
    def test_negative_auth_user(self, condition):          # в тесте будем вызывать переменную condition со значениями словаря exclude_params
        # далее идёт код со значениями из списка exclude_params, где мы передаём в запрос только параметр с куки или токеном
        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                     headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth", cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(response2, "user_id", 0, f"User is authorized with condition {condition}")
