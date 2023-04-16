import requests

response = requests.post("https://playground.learnqa.ru/api/check_type")   # code response 200
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_500")      # code response 500
print(response.status_code)
print(response.text)                                                       # None

response = requests.post("https://playground.learnqa.ru/api/dontpanic")    # code response 404
print(response.status_code)
print(response.text)                                                       # This is 404 error! <a href='/'>Home</a>


response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)                                                # 301 (не позволяет редирект - статус False)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response.status_code)                                                # 200 (позволяет редирект - статус True )
print(response.history)                                                    # [<Response [301]>]

# allow_redirects - аргумент включающий(True) либо исключающий(False), редирект при статусе кода ответа -  301
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response
print(first_response.url)                       # https://playground.learnqa.ru/api/get_301
print(second_response.url)                      # https://www.learnqa.ru/

# headers
headers = {"simple_headers": "dont panic"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
print(response.text)                            # заголовки запроса
print(response.headers)                         # заголовки ответа
# для удобства принт заголовков можно скопировать и посмотреть тут https://jsonviewer.stack.hu





