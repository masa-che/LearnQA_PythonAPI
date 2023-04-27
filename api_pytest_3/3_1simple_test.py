class TestExample:
    def test_check_math(self):
        a = 4
        b = 4
        expected_sum = 8
        assert a+b == expected_sum, "Sum of variable isn't equal"

    def test_check_error(self):
        a = 4
        b = 3
        expected_sum = 8
        assert a+b == expected_sum, "Sum of variable isn't equal"

# python -m pytest api_pytest_3\3_1simple_test.py
