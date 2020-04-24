import pytest


@pytest.fixture
def expected_name_breweries_san_diego():
    return ['Abnormal Beer Company', 'Brewery in Planning - San Diego',
            'Eppig Brewing', 'Mike Hess Brewing - Miramar',
            'New English Brewing Co Inc',
            'Stone Brewing World Bistro & Gardens- Liberty Station',
            'Thunderhawk Alements', 'Alta Brewing Company',
            '32 North Brewing Co', '10 Barrel Brewing Co',
            '2Kids Brewing Company', 'Acoustic Ales Brewing Experiment',
            'AleSmith Brewing Co', 'Amplified Ale Works Miramar Studio',
            'Align Brewing Co', 'Amplified Ale Works',
            'Ballast Point Brewing Co / Home Brew Mart', 'Barn Brewery',
            'Ballast Point Brewing Company', 'Ballast Point Brewing Company']


@pytest.fixture
def expected_name_breweries_tucson():
    return ['1912 Brewing', 'BlackRock Brewers', 'Dragoon Brewing Co', 'Button Brew House, LLC',
            'Catalina Brewing Company', 'Copper Mine Brewing Co', 'Barrio Brewing Co',
            'Corbett Brewing Company', 'Crooked Tooth Brewing Co.', 'Dillinger Brewing Company',
            "Iron John's Brewing Company", 'Green Feet Brewing', 'Public Brewhouse',
            'Pueblo Vida Brewing Co', 'Ten Fifty Five Brewing', 'Thunder Canyon Brewery',
            'Sentinel Peak Brewing Company', 'Borderlands Brewing Co',
            'The Address Brewing / 1702 Beer & Pizza']


def test_brewer_by_city(call_api, pytestconfig, expected_name_breweries_tucson, expected_name_breweries_san_diego):
    city = pytestconfig.getoption("--city")
    if city:
        city = {'by_city': city}

    response = call_api.get_method(path='/breweries', params=city)
    data = response.json()
    name_breweries = []
    for val in data:
        name_breweries.append(val['name'])

    if city['by_city'] == 'san_diego':
        assert expected_name_breweries_san_diego == name_breweries
    elif city['by_city'] == 'tucson':
        assert expected_name_breweries_tucson == name_breweries
