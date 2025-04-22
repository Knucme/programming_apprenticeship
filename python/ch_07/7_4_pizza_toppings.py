active = True

while active:
    topping = input("Enter a topping: ")

    if topping.lower() == "quit":
        break
    else:
        print(f"I will add {topping}!")

