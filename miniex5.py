import random

class Dice:
    def roll(self):
        randoms01 =random.randint(1,10)
        randoms02 =random.randint(1,10)
        return randoms01,randoms02
dice=Dice()
print(dice.roll())

