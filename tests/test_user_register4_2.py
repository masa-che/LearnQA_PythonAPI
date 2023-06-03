import requests
from Key_Frame_Classes.base_case import BaseCase
from Key_Frame_Classes.assertions import Assertions
from datetime import datetime

# создание нового пользователя (операции с email, новый создаваемый пользователь с рандомной частью email)


class TestUserRegister(BaseCase):
    def setup_method(self):                           # метод генерации email для создаваемого пользователя
        base_part = "learnqa"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        domain = "example.com"
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):          # позитивный тест регистрации пользователя
        data = {
            'password': 'qwerty123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_status_code(response, 200)    # делаем проверку из assertions.py что status_code == 200
        print(response.content)                         # получим json id нового пользователя (в assertions.py пишем проверку для поля id )
        Assertions.assert_json_has_key(response, "id")  # делаем проверку из assertions.py что name - "id" существует

    # запуск конкретного метода из теста через терминал pycharm:
    # python -m pytest -s tests/test_user_register4_2.py -k test_create_user_successfully

    def test_create_user_with_existing_email(self):   # негативный тест на регистрацию уже существующего пользователя
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
        Assertions.assert_status_code(response, 400)  # делаем проверку из assertions.py что status_code == 400
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists",\
            f"Unexpected response content {response.content}"

# python -m pytest -s tests/test_user_register4_2.py
