import requests
import pytest

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


# Задача 13. User_Agent

class TestUserAgent:
    user_agent_information = [
        {
            "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "platform": "Mobile",
            "browser": "No",
            "device": "Android"},
        {
            "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "platform": "Mobile",
            "browser": "Chrome",
            "device": "iOS"},
        {
            "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "platform": "Googlebot",
            "browser": "Unknown",
            "device": "Unknown"},
        {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "platform": "Web",
            "browser": "Chrome",
            "device": "No"},
        {
            "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "platform": "Mobile",
            "browser": "No",
            "device": "iPhone"}
    ]

    @pytest.mark.parametrize("user_agent_data", user_agent_information)
    def test_user_agent(self, user_agent_data):
        user_agent = user_agent_data["user_agent"]
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                headers={"User-Agent": user_agent})

        actual_result = response.json()
        print(actual_result)
        assert actual_result['platform'] in user_agent_data['platform'],\
            f"The '{actual_result['platform']}' does not match the expected result"
        assert actual_result['browser'] in user_agent_data['browser'],\
            f"The '{actual_result['browser']}' does not match the expected result"
        assert actual_result['device'] in user_agent_data['device'],\
            f"The '{actual_result['device']}' does not match the expected result"
