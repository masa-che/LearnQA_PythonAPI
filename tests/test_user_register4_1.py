import requests
from Key_Frame_Classes.base_case import BaseCase
from Key_Frame_Classes.assertions import Assertions


# проверка реакции сервера на существующий email


class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': 'qwerty123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
# данные отправляем post запросом на наш метод
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        print(response.status_code)  # 400
        print(response.content)      # b"Users with email 'vinkotov@example.com' already exists"
# получив b (байтовую строку необходимо переформатировать её, для сравнения со строкой, применив - .decode("utf-8") )
        assert response.status_code == 400,\
            f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",\
            f"Unexpected response content {response.content}"
# python -m pytest -s tests/test_user_register4_1.py



