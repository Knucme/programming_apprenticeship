

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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """Represents aspects of a restaurant, specific to an Icecream Stand"""
        super().__init__(restaurant_name, cuisine_type)
       
        self.flavors_available = [
                "Vanilla", "Chocolate", "Strawberry",
                        "Mint Chocolate Chip", "Butter Pecan",
                        "Chocolate Chip Cookie Dough"
                        ]
    def flavors(self):
        """Displays all the flavors available"""
        print("Flavor Menu:")
        for flavor in self.flavors_available:
            print(f"- {flavor}")

store1 = IceCreamStand("The Ice Cream Stop", "Ice Cream")
store1.flavors()



