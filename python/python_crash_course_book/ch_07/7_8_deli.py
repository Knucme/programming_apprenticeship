sandwich_orders = ["italian roast beef", "BLT", "Tuna", "Meatballs"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop().title()

    print(f"I made your {sandwich} sandwich!")

    finished_sandwiches.append(sandwich)

print("Completed Sandwiches: ")

for sandwich in finished_sandwiches:
    print(sandwich)
