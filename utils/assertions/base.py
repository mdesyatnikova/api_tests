import allure


@allure.step("Checking status code")
def assert_status_code(actual, expected):
    assert actual == expected, f'Request failed with status code {actual}, but must be {expected}'


@allure.step("Checking {field_name} in response")
def assert_response_value(actual, field_name, expected_value):
    value = actual.get(field_name)
    assert value == expected_value, f'Value {field_name} = {actual}, but must be {expected_value}'
