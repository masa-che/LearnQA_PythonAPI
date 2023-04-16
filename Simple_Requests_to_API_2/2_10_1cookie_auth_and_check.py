import requests

payload = {"login": "secret_login", "password": "secret_pass"}                                   # параметр dict{}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)      # ответ на post запрос

cookie_value = response.cookies.get('auth_cookie')             # забираем значение cookie из dict по ключу 'auth_cookie'
                                                               # {'auth_cookie': '554340'}

cookies = {}                                                   # словарь (массив) для cookie
if cookie_value is not None:                                   # если пара логин/пароль не верна, вернёт None, мы работаем с значением cookie_value is not None
    cookies.update({'auth_cookie': cookie_value})              # обновление значения cookies для проверки в след запросе

response1 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)  #ответ на post запрос

print(response1.text)                                          # You are authorized
