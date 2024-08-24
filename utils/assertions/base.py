def assert_status_code(actual, expected):
    assert actual == expected, f'Request failed with status code {actual}, but must be {expected}'
