from restaurant import Restaurant
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



