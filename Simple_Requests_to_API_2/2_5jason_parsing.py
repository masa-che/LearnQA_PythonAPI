import json

string_as_json_format = '{"answer":"Hello, User"}'     # json формат, обернули в переменную, перед преобразованием
obj = json.loads(string_as_json_format)                # методом loads преобр нашу строку из json в объект python {dict}
# print(obj['answer'])                                 # в словаре (obj) по ключу, принтуем значение данного словаря
key = "answer"
if key in obj:                                         # если ключ есть в объекте:
    print(obj[key])                                    # принтуем из словаря(obj) по ключу key, значение данного словаря
else:                                                  # иначе:
    print(f"Key {key} in JSON not found")              # принтуем, что ключа key в json не найден

