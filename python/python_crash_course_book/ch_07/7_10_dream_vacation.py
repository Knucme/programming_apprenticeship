poll = True
people_polled = {}

while poll:
    name = input("Name: ")
    dream_vacation = input("Dream Vacation Location: ")

    people_polled[name] = dream_vacation

    cont = input("Contine y/n: ")

    if cont.lower() == 'n':
        poll = False


for key, item in people_polled.items():
    print(f"{key} dream vacation is {item}")

