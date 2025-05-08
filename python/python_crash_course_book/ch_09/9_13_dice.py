from random import random, randrange

class Dice:
    """This class will model a dice."""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self, num_rolls=1):
        """Will simulate a rolled dice"""
        for roll in range(1,num_rolls + 1):
            print(f"Roll #{roll}: {randrange(1,self.sides,1)}")

print("6 sided dice being rolled...")
dice06 = Dice().roll_dice(10)
dice10 = Dice()
dice10.sides = 10
print("10 sided dice being rolled...")
dice10.roll_dice(10)
dice20 = Dice()
dice20.sides = 20   
print("20 sided dice being rolled...")
dice20.roll_dice(10)
