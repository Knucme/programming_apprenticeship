from random import choice
num_lst = [1, 100, 60, 88, 76, 44, 55,70,800, 100000, 'a', 't','r','K', 'y']
winning_lst = []
count = 0
for i in range(1, 6):
    winning_lst.append(choice(num_lst))

print(f"Any ticket matching these 4 numbers or letters wins a prize:\n{winning_lst}")

while(True):
    selection_lst = []
    
    for i in range(1,6):
        selection_lst.append(choice(num_lst))

    if selection_lst == winning_lst:
        print(f"Winner!!! and it only took {count} tries!")
        break;
    print("Loser!!!")
    count += 1
