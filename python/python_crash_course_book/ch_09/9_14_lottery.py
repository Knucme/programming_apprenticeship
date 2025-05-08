from random import choice
num_lst = [1, 100, 60, 88, 76, 44, 55,70,800, 100000, 'a', 't','r','K', 'y']
num_selections = []

for i in range(1, 6):
    num_selections.append(choice(num_lst))

print(f"Any ticket matching these 4 numbers or letters wins a prize:\n{num_selections}")
