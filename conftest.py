import pytest
import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_method(self, path='/', params=None):

        url = f'{self.base_url}{path}'
        # print(params)
        # print(url)
        res = requests.get(url=url, params=params)
        # print(res.url)
        return res


def pytest_addoption(parser):
    parser.addoption(
        '--base_url',
        default='https://api.openbrewerydb.org',
    )

    parser.addoption(
        '--city',
        default='san_diego',
        choices='san_diego, tucson'
    )


@pytest.fixture(scope='session')
def call_api(request):
    base_url = request.config.getoption('--base_url')
    yield APIClient(base_url=base_url)
    print('\nTest finished')
