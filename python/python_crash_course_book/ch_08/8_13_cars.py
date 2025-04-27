def cars(manufacturer, model, **car_values):
    car_values["manufacturer"] = manufacturer
    car_values["model"] = model

    return car_values

car = cars("Subaru", "Outback", color="blue", tow_package=True)
print(car)
