from cities.city_functions import city

def test_city_country():
    city_name = city('Santiago', 'Chile')
    assert city_name == 'Santiago, Chile'

def test_city_country_population():
    city_name = city('santiago', 'chile', 5000000)
    assert city_name == 'santiago, chile - population 5000000'

