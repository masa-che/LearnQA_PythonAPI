import requests

payload = {"login": "secret_login", "password": "secret_pass"}                               # параметр dict{}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)  # ответ на post запрос

print(response.text)                            #
print(response.status_code)                     # 200
print(dict(response.cookies))                   # {'auth_cookie': '554340'}
print(response.headers)                         # {
                                                # 'Date': 'Sat, 15 Apr 2023 11:18:28 GMT',
                                                # 'Content-Type': 'text/html; charset=utf-8',
                                                # 'Content-Length': '0',
                                                # 'Connection': 'keep-alive',
                                                # 'Keep-Alive': 'timeout=10',
                                                # 'Server': 'Apache',
                                                # 'Set-Cookie': 'auth_cookie=131292; expires=Tue, 16-May-2023 11:18:28 GMT; Max-Age=2678400; path=/; domain=playground.learnqa.ru; HttpOnly',
                                                # 'Cache-Control': 'max-age=0',
                                                # 'Expires': 'Sat, 15 Apr 2023 11:18:28 GMT'
                                                # }
