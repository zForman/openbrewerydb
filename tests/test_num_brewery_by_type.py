import pytest


@pytest.mark.parametrize('params', [('planning', 20),
                                    ('micro', 20),
                                    ('regional', 20)])
def test_number_brewery_by_type(call_api, params):
    query = {'by_type': params[0]}
    response = call_api.get_method(path='/breweries', params=query)
    data = response.json()
    assert len(data) == params[1]
