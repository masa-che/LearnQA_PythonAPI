import requests
import json
import time

# Задача 5 Парсинг JSON
# Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную json_text
# и вывести текст второго сообщения с помощью функции print.

# json формат, обернули в переменную, перед преобразованием
string_as_json_format = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},' \
                        '{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(string_as_json_format)                # метод loads преобразует строку из json в объект python {dict}
print(obj['messages'][1])                              # в словаре (obj) по ключу, принтуем 2-е сообщение

# Задача 6 Длинный редирект

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
check_response = response.history
print(check_response)                               # [<Response [301]>, <Response [301]>] (один редирект)
response = response.history[1]                      # или [-1] - последний элемент из списка
print(response.url)                                 # https://playground.learnqa.ru/ (конечный url)
response = requests.get("https://playground.learnqa.ru/api/long_redirect")

# Задача 7  Запросы и методы
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


# Задача 8 - "Токены"
# 8.1 Скрипт создаёт задачу: с полем token и second, токен как параметр мы будем отправлять в 8.2, секунды в 8.3_4
URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(URL)
response_json = response.text
print(response_json)                   # {"token":"QNwoTNzoDMyASMy0CNw0yMyAjM","seconds":15}
obj = json.loads(response_json)        # методом loads преобразовывает нашу строку из json в объект python {dict}
token = obj['token']
seconds = obj['seconds']               # секунды нужны будут для ожидания
print(obj['token'])                    # AO0ozM0oDMyASMy0CNw0yMyAjM

# 8.2 Скрипт должен делать один запрос с token ДО того, как задача готова, убеждался в правильности поля status
response = requests.get(URL, params={"token": token})
response_json = response.text
print(response_json)                   # {"status":"Job is NOT ready"}
obj = json.loads(response_json)        # {'status': 'Job is NOT ready'}
if obj['status'] == "Job is NOT ready":
    print("expected status")
else:
    print("not expected status")

# 8.3_4 скрипт ждал бы нужное количество секунд с помощью функции time.sleep(), затем делал бы один запрос c token
# ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
time.sleep(seconds)

response = requests.get(URL, params={"token": token})
response_json = response.text
print(response_json)                   # {"result":"42","status":"Job is ready"}

obj = json.loads(response_json)        # {'status': 'Job is NOT ready'}
if obj['status'] == "Job is ready" and obj['result'] == "42":
    print("expected result - 42 and status - Job is ready")
else:
    print("not expected result")

# Задача 9 "Подбор пароля"
# Данные из статьи в википедии "Top 25 most common passwords by year according to SplashData"
password_str = " password 123456 123456789 12345678 12345 qwerty abc123 qwerty football" \
               " 1234567 monkey 111111 letmein 1234 1234567890" \
               " 1234567	12345letmein	dragon	1234567	baseball	1234	1234567	1234567	sunshine" \
               " iloveyou trustno1	111111	iloveyou	dragon	1234567	princess	football	qwerty" \
               " 111111 dragon	baseball	adobe123[a]	football	baseball	1234	iloveyou	iloveyou" \
               " 123123" "baseball	iloveyou	123123	1234567	welcome	login	admin	princess" \
               " abc123 111111	trustno1	admin	monkey	1234567890	welcome	welcome	admin	" \
               " qwerty123 iloveyou	1234567	1234567890	letmein	abc123	solo	monkey	welcome	1q2w3e4r master" \
               " sunshine	letmein	abc123	111111	abc123	login	666666	admin sunshine	master	photoshop[a]" \
               " 111111	1qaz2wsx	admin	abc123	abc123	qwertyuiop ashley	123123	1234	mustang	dragon" \
               " 121212	starwars	football	654321 bailey	welcome	monkey	access	master" \
               " flower	123123	123123	555555 passw0rd	shadow	shadow	shadow	monkey	passw0rd" \
               " dragon	monkey	lovely shadow	ashley	sunshine	master	letmein	dragon	passw0rd" \
               " 654321	7777777 123123	football	12345	michael	login	sunshine	master	!@#$%^&*" \
               " welcome 654321	jesus	password1	superman	princess	master	hello	charlie" \
               " 888888 superman	michael	princess	696969	qwertyuiop	hottie	freedom	aa123456" \
               " princess qazwsx	ninja	azerty	123123	solo	loveme	whatever	donald	dragonmichael" \
               " mustang	trustno1 batman	passw0rd	zaq1zaq1	qazwsx	password1	password1 Football" \
               " password1	000000	trustno1	starwars	password1	trustno1	qwerty123	123qwe"
print(password_str.split())                                # split создаёт список и каждое слово в str разделяет запятой
print(len(password_str.split()))                           # длина списка 172 - элемента
password_list = password_str.split()
top_password_list = []
[top_password_list.append(x) for x in password_list if x not in top_password_list]  # редактирование списка, для "устранения" повторяющихся эл-ов
print(top_password_list)                                   # при помощи нового списка убрали повторения
print(len(top_password_list))                              # длина нового списка 72 - элемента

URL = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
for password in top_password_list:
    response = requests.post(URL, data={"login": "super_admin", "password": password})
    # print(response.cookies)
    cookie_value = response.cookies.get('auth_cookie')     # забираем значение cookie из dict по ключу 'auth_cookie'
    cookie = {'auth_cookie': cookie_value}
    check_response = requests.post('https://playground.learnqa.ru/ajax/api/check_auth_cookie', cookies=cookie)
    check_auth = check_response.text
    # print(check_auth)                               # проверка текстового ответа перебора 72 эл-в "You are authorized"
    if check_auth == "You are authorized":
        print(f"{check_auth} password = {password}")
