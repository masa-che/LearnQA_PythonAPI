import requests


# Задача 10. Тест на короткую фразу не больше 15ти символов.

class Test:
    def test_input_phrase(self):
        phrase = input("Set a phrase: ")
        expected_len_phrase = 15
        assert len(phrase) <= expected_len_phrase, "Phrase > 15 simbols"

# python -m pytest -s api_pytest_3\test_hw.py

