import requests

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# Задание 1 если не использовать параметры для всех типов запроса:

requests_list = ["GET", "POST", "PUT", "DELETE"]
for method in requests_list:
    response = requests.request(method, URL)
    print(f"текст ответа - {response.text}, статус код -  {response.status_code}")
    # текст ответа - Wrong method provided, статус код -  200 (для всех типов http запроса)

# Задание 2 если запрос не из списка:

response_head = requests.head(URL)
print(f"текст ответа - {response_head.text}, статус код -  {response_head.status_code}")


# Задание 3 скрипт делает запрос с правильным значением method:

list_req_param = ["GET", "POST", "PUT", "DELETE"]
for request_type in list_req_param:
    for parameter in list_req_param:
        if request_type == parameter:
            response = requests.request(request_type, URL, params={"method": {parameter}})
            print(f"method-{request_type},params-{parameter},status code-{response.status_code},response server-{response.text}")
# запрос GET с 'method': 'GET', имеет статус код 200 текст ответа {"success":"!"}
# (и тд для всех типов запроса совпадающих со значением параметра)

print()

# Задание 4, с помощью цикла скрипт проверяет все возможные сочетания реальных типов запроса и значений параметра method
# Например, с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. 4.1 Найти такое сочетание, когда тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. 4.2 Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

list_req_param = ["GET", "POST", "PUT", "DELETE"]
for request_type in list_req_param:
    for parameter in list_req_param:
        if request_type == "GET" and parameter != "GET":
            response = requests.request(request_type, URL, params={"method": {parameter}})
            print(f"method-{request_type},params-{parameter},status code-{response.status_code},response server-{response.text}")
        elif request_type != parameter:
            response = requests.request(request_type, URL, data={"method": {parameter}})
            print(f"method-{request_type},data-{parameter},status code-{response.status_code},response server-{response.text}")
# ответ 4.1 method-DELETE,data-GET,status code-200,response server-{"success":"!"} -
# тип запроса не совпадает с параметром но сервер отвечает всё ок.

# ответ 4.2 при совпадении http запроса (из списка) и значения параметра, сервер отвечает {"success":"!"}
