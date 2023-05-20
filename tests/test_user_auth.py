import requests
import pytest

from Key_Frame_Classes.base_case import BaseCase


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
        response0 = requests.get(url, headers={"x-csrf-token": self.token}, cookies={"auth_sid": self.auth_sid})

        assert "user_id" in response0.json(), "user_id not found"

        user_id_from_check_method = response0.json()["user_id"]
        print(user_id_from_check_method)

        assert self.user_id_from_auth_method == user_id_from_check_method, "user_id not equal"

    # негативная проверка на авторизацию

    @pytest.mark.parametrize('condition', exclude_params)  # подключаем в виде параметра exclude_params и
    def test_negative_auth_user(self, condition):          # в тесте будем вызывать переменную condition со значениями словаря exclude_params
        # далее идёт код со значениями из списка exclude_params, где мы передаём в запрос только параметр с куки или токеном
        if condition == "no_cookie":
            response0 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                     headers={"x-csrf-token": self.token})
        else:
            response0 = requests.get("https://playground.learnqa.ru/api/user/auth", cookies={"auth_sid": self.auth_sid})

        assert "user_id" in response0.json(), "There no user id in the response"

        user_id_from_check_method = response0.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"

