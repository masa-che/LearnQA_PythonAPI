import requests


# Задача 10. Тест на короткую фразу не больше 15ти символов.

class Test:
    def test_input_phrase(self):
        phrase = input("Set a phrase: ")
        expected_len_phrase = 15
        assert len(phrase) <= expected_len_phrase, "Phrase > 15 simbols"

# python -m pytest -s api_pytest_3\test_hw.py


# Задача 11. Тест запроса на метод cookie

class TestRequestMethodCookie:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        check_cookies = dict(response.cookies)       # используем dict что бы при принте cookie были в виде словаря
        print(check_cookies)                         # {'HomeWork': 'hw_value'}
        print(check_cookies['HomeWork'])             # hw_value
        expected_response_cookies = 'hw_value'
        assert check_cookies['HomeWork'] == expected_response_cookies, "Wrong value cookie"


# Задача 12. Тест запроса на метод header

class TestRequestMethodHeader:
    def test_check_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        response_text = response.text
        print(response_text)               #{"success":"!"}
        response_json = response.json
        print(response_json)               # <bound method Response.json of <Response [200]>>
        response_header = response.headers
        print(response_header)             # {
                                           # 'Date': 'Fri, 28 Apr 2023 13:11:48 GMT',
                                           # 'Content-Type': 'application/json',
                                           # 'Content-Length': '15',
                                           # 'Connection': 'keep-alive',
                                           # 'Keep-Alive': 'timeout=10',
                                           # 'Server': 'Apache',
                                           # 'x-secret-homework-header': 'Some secret value',
                                           # 'Cache-Control': 'max-age=0',
                                           # 'Expires': 'Fri, 28 Apr 2023 13:11:48 GMT'
                                           # }
        # просто было интересно, вернут в ответе text, посмотреть сам json, . Теперь возьмём значение в словарь headers
        check_header = response.headers['x-secret-homework-header']
        print(check_header)                # Some secret value
        assert check_header == 'Some secret value', "Wrong value header 'x-secret-homework-header'"



