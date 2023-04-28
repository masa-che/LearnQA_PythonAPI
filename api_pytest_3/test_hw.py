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
        check_cookie = dict(response.cookies)
        print(check_cookie)                         # {'HomeWork': 'hw_value'}
        print(check_cookie['HomeWork'])             # hw_value
        expected_response_cookie = 'hw_value'
        assert check_cookie['HomeWork'] == expected_response_cookie, "Wrong value cookie"





