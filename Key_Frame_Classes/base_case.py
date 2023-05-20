import json.decoder

from requests import Response
# в классе будут содержаться методы для получения куки и хедеров из ответов сервера по имени
# суть методов - в метод мы передаём объект ответа, который мы получаем после запроса
# и имя в результате которого мы будем получать либо хедер, либо куки

# функции get_cookie/header будут возвращать имена содержащиеся в Response для дальнейшей проверки авторизации клиента
class BaseCase:
    def get_cookie(self, response: Response, cookie_name):# объект ответа Response содержит всю информацию, возвращаемую сервером
        assert cookie_name in response.cookies, f"Can't find cookie with name {cookie_name}"
        return response.cookies[cookie_name]               # возвращаем cookie_name

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Can't find header with name {headers_name}"
        return response.headers[headers_name]

# функция get_json_value принимает ответ названия поля в json имя которого мы хотим получить, из общего Response
    def get_json_value(self, response: Response, name):
        try:                                              # проверяем что ответ пришёл в формате JSON
            response_as_dict = response.json()
        except json.decoder.JSONDecoderError:             # если не в формате JSON тест упадёт и напишет текст ошибки из assert
            assert False, f"Response is not JSON format. Response text is  '{response.text}'"
                                                          # если try отработал - проверка нахождения name
        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]
