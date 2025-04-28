class Restaurant:
    """This a model of a restaurant menu"""

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """prints two attributes out to console"""

        print(f"Restaurant name is {self.restaurant_name}")
        print(f"Cuisine type served is {self.cuisine_type}")

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open"""

        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, num):
        """Sets the number of people served!""" 
        self.number_served = num
    
    def increment_number_served(self, increment_amt):
        """Increments the number of people served by a user amount."""
        self.number_served += increment_amt


restaurant = Restaurant("Burger King", "Burgers")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10000)
print(restaurant.number_served)
restaurant.increment_number_served(100)
print(f"100 more people arrived at closing time which brought up our total served to {restaurant.number_served}")
