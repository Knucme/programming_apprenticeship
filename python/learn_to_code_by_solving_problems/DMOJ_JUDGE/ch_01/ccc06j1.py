burger = int(input())
side = int(input())
drink = int(input())
dessert =  int(input())

calorie_meal_total = 0

if burger == 1:
    calorie_meal_total += 461
elif burger == 2:
    calorie_meal_total += 431
elif burger == 3:
    calorie_meal_total += 420
else:
    calorie_meal_total += 0

if side == 1:
    calorie_meal_total += 100
elif side == 2:
    calorie_meal_total += 57
elif side == 3:
    calorie_meal_total += 70
else:
    calorie_meal_total += 0

if drink == 1:
    calorie_meal_total += 130
elif drink == 2:
    calorie_meal_total += 160
elif drink == 3:
    calorie_meal_total += 118
else:
    calorie_meal_total += 0

if dessert == 1:
    calorie_meal_total += 167
elif dessert == 2:
    calorie_meal_total += 266
elif dessert == 3:
    calorie_meal_total += 75
else:
    calorie_meal_total += 0

print(f"Your total Calorie count is {calorie_meal_total}.")
