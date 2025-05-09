def city(city_name, country_name, population=0):

    if population >0:
        return f"{city_name}, {country_name} - population {population}"
    else:
        return f"{city_name}, {country_name}"

