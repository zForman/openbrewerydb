import pytest


def query():
    return ['dog', 'Address', 'Home', 'Acoustic', 'Company']


@pytest.mark.parametrize('params', query())
def test_autocomplete(call_api, params):
    query = {'query': params}
    response = call_api.get_method(path='/breweries/autocomplete', params=query)
    data = response.json()

    if len(data) == 0:
        raise ValueError("Wrong query")
    assert response.reason == 'OK'


@pytest.mark.parametrize('params', query())
def test_search(call_api, params):
    query = {'query': params}
    response = call_api.get_method(path='/breweries/search', params=query)
    data = response.json()

    if len(data) == 0:
        raise ValueError("Wrong query")
    assert response.reason == 'OK'
