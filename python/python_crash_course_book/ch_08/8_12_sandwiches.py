def toppings(*arg):
    print("The Sandwich will have the following items: ")
    for item in arg:
        print(f"- {item}")

toppings("apples", "nuggets", "chicken", "oranges")
toppings("beer")
toppings("buggers", "candy", "bee's", "sugar", "money", "chicken", "sand")
