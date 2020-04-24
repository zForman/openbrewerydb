import pytest
from jsonschema import validate
import json


@pytest.mark.parametrize('path', ['/breweries/5485',
                                  '/breweries/5487',
                                  '/breweries/5488',
                                  '/breweries/5490',
                                  '/breweries/5492',
                                  '/breweries/5493',
                                  '/breweries/5494'])
def test_single_brewery_schema_validation(call_api, path):
    response = call_api.get_method(path=path)
    data = response.json()

    with open('test_single_brewery_schema.json', 'r') as f:
        schema_data = f.read()
    json_schema = json.loads(schema_data)

    validate(instance=data, schema=json_schema)
