import pytest

from base.client import Client


@pytest.fixture(scope='session')
def client(base_url):
    return Client(base_url)


@pytest.fixture(scope='session', autouse=True)
def base_url(request):
    return request.config.getoption('--url')


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://rahulshettyacademy.com')
