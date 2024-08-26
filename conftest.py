import pytest

from base.client import Client
from utils.functions.base import package_contents, load_from_module


@pytest.fixture(scope='session')
def client(base_url):
    return Client(base_url)


@pytest.fixture(scope='session', autouse=True)
def base_url(request):
    return request.config.getoption('--url')


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://rahulshettyacademy.com')


def pytest_generate_tests(metafunc):
    testdata = []
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_dir = str(metafunc.definition.path).replace('\\', '/').split('/')
            path = '.'.join(test_dir[test_dir.index('tests') + 1:-1])
            module = fixture[5:]
            submodules = package_contents(path, module)
            if isinstance(submodules, str):
                testdata = load_from_module(path, submodules)
            else:
                for submodule in submodules:
                    module_data = load_from_module(path, submodule)
                    testdata.extend(module_data)
            metafunc.parametrize(fixture, testdata, ids=[repr(x) for x in testdata])
