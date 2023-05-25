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

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"  # проверка того что необходимое имя есть в отете формата json
        assert response_as_dict[name] == expected_value, error_message               # сравнеие полученного результата имени с ожидвемым

