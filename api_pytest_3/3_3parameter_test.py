import pytest
import requests


class TestFirstApi:
    names = [
        ("Dar Veter"),
        ("Erg Noor"),
        ("Niza Krit"),
        ("Veda Kong"),
        ("")

    ]

    # 'name' - переменная в которую будут последовательно вложены значения из списка names
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        print(response_dict)                        # {'answer': 'Hello, Dar Veter'} и так далее для всех имён
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = f"Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict['answer']
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"
