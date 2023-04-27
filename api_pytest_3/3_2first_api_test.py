import requests


class TestFirstApi:
    def test_hello_call(self):
        url = 'https://playground.learnqa.ru/api/hello'
        name = 'Dar Veter'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        print(response_dict)                        # {'answer': 'Hello, Dar Veter'}
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict['answer']
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"

# python -m pytest api_pytest_3\3_2first_api_test.py
