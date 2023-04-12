import requests

payload = {"name": "player_one"}                                                     # параметр dict{}
response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)   # get запрос к url адресу
print(response.text)                                                                 # print в формате json

