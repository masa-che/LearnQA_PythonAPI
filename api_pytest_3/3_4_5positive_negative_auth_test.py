import requests
import pytest


# Первый запрос - "sign_in" с передачей email и password (получаем в ответе необходимые для чека аутентификации данные)
class TestPositiveAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        check_cookie = dict(response.cookies)
        print(check_cookie)           # {'auth_sid': 'ff4177f4405054f11719b0ae92cafcb902e94918f1549272bcf2cafc2634fd9d'}              # нужный нам auth_sid (динамичен)
        check_headers = response.headers
        print(check_headers)            # {
                                        # 'Set-Cookie': 'auth_sid=ff4177f4405054f11719b0ae92cafcb902e94918f1549272bcf2cafc2634fd9d',  # (динамичен)
                                        # 'x-csrf-token': '0110f25aef0280470ffd419533df5d058ffc246902e94918f1549272bcf2cafc2634fd9d', # нужный нам token (динамичен)
                                        # 'Cache-Control': 'max-age=0',
                                        # 'Expires': 'Sat, 29 Apr 2023 11:39:08 GMT'
                                        # }

        check_json = response.json()
        print(check_json)               # {'user_id': 2}    # нужный нам user_id (статичен)

        assert 'auth_sid' in response.cookies, "cookie not found"
        assert 'x-csrf-token' in response.headers, "token not found"
        assert 'user_id' in response.json(), "There no user id in the response"

# Второй запрос - "проверка успешной авторизации пользователя" из первого запроса здесь используются след переменные:
        auth_sid = response.cookies.get('auth_sid')            # ff4177f4405054f11719b0ae92cafcb902e94918f1549272bcf2cafc2634fd9d
        token = response.headers.get('x-csrf-token')           # 0110f25aef0280470ffd419533df5d058ffc246902e94918f1549272bcf2cafc2634fd9d
        user_id_from_auth_method = response.json()['user_id']  # 2
        print(auth_sid, token, user_id_from_auth_method)

        url = "https://playground.learnqa.ru/api/user/auth"
        response0 = requests.get(url, headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})
        print(response.json()['user_id'])                      # 2
        assert 'user_id' in response0.json(), "user_id not found"
        user_id_from_check_method = response0.json()['user_id']
        assert user_id_from_auth_method == user_id_from_check_method, "user_id not equal"


# Задание 3_4_5 Негативные тесты на авторизацию пользователя
    exclude_params = {
        'no_cookie',
        'no_token'
    }

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_user(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert 'auth_sid' in response.cookies, "cookie not found"
        assert 'x-csrf-token' in response.headers, "token not found"
        assert 'user_id' in response.json(), "There no user id in the response"

        auth_sid = response.cookies.get('auth_sid')
        token = response.headers.get('x-csrf-token')



