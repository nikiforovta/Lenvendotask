import pytest

from api.client import JsTestTaskApiClient
from api.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://lenvendo.ru')


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope='session')
def config(request):
    return {'url': request.config.getoption('--url')}


@pytest.fixture(scope="function")
def api_client() -> JsTestTaskApiClient:
    api_client = JsTestTaskApiClient()
    return api_client
