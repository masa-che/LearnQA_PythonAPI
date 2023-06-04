from requests import Response
import json

# def assert_json_value_by_name мы хотим убедиться что значение внутри json доступно по определённому имени
# и равняется тому, чему мы ожидаем
# декоратором оборачиваем функцию, т.к. class Assertions не является прямым наследником для тестов.
# удобнее использовать его функции как статические


class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()  # проверяем что ответ пришёл в формате JSON
        except json.JSONDecodeError:            # если не в формате JSON выдаст ошибку и напишет текст ошибки из assert
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"  # проверка того что необходимое имя есть в ответе формата json
        assert response_as_dict[name] == expected_value, error_message               # сравнеие полученного результата имени с ожидвемым

    @staticmethod
    def assert_json_has_key(response: Response, name):     # метод проверки получения в json поля id нового пользователя
        try:
            response_as_dict = response.json()  # проверяем что ответ пришёл в формате JSON
        except json.JSONDecodeError:            # если не в формате JSON выдаст ошибку и напишет текст ошибки из assert
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"  # проверка того что необходимое имя есть в ответе формата json

    @staticmethod
    def assert_json_has_not_key(response: Response, name):  # метод проверки отсутствия полей(ключей) в json (4_3)
        try:
            response_as_dict = response.json()  # проверяем что ответ пришёл в формате JSON
        except json.JSONDecodeError:  # если не в формате JSON выдаст ошибку и напишет текст ошибки из assert
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'"  # проверка того что необходых имён нет в ответе формата json

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):  # метод проверки получения в json полей(ключей) пользователя (4_3)
        try:
            response_as_dict = response.json()  # проверяем что ответ пришёл в формате JSON
        except json.JSONDecodeError:  # если не в формате JSON выдаст ошибку и напишет текст ошибки из assert
            assert False, f"Response is not JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"  # проверка того что необходимое имя()ключ есть в ответе формата json

    @staticmethod                                                # метод сравнения статус кода, задание (4_2)
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code,\
            f"Unexpected status code, expected: {expected_status_code}, actual: {response.status_code}"
