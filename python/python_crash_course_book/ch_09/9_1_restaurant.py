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

restaurant = Restaurant("Burger King", "Burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()
