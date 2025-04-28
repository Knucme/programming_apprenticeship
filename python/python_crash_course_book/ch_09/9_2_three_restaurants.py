class Restaurant:
    """This a model of a restaurant menu"""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints two attributes out to console"""

        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type served is {self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open"""

        print(f"{self.restaurant_name} is now open!")

restaurant_01 = Restaurant("Burger King", "Burgers")
restaurant_01.describe_restaurant()
restaurant_01.open_restaurant()

restaurant_02 = Restaurant("Red Lobster", "Seafood")
restaurant_02.describe_restaurant()
restaurant_02.open_restaurant()

restaurant_03 = Restaurant("Outback", "Steakhouse")
restaurant_03.describe_restaurant()
restaurant_03.open_restaurant()
