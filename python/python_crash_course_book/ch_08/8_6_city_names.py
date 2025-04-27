def city_country(city_name, country):
    locations = {
            "city name": city_name,
            "country": country,
            }
    return locations

print(city_country("Santiago", "Chile"))
print(city_country("San Diego", "California"))
print(city_country("Mexico City","Mexico"))


