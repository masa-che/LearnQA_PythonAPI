import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"name": "User"})
print(response.text)                                # для get - используется params

response = requests.put("https://playground.learnqa.ru/api/check_type", data={"name": "User"})
print(response.text)                                # для post, put, delete  - используется data

# status code
response = requests.post("https://playground.learnqa.ru/api/check_type")   # code response 200
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_500")      # code response 500
print(response.status_code)
print(response.text)                                                       # None

response = requests.post("https://playground.learnqa.ru/api/dontpanic")    # code response 404
print(response.status_code)
print(response.text)                                                       # This is 404 error! <a href='/'>Home</a>


response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
print(response.status_code)
