#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Player - Class model
   Cheat_Swapper(Player) - Subclass model
   Cheat_Loaded_Dice(Player) - Subclass model
   continuing with dice game from lab 74"""

#from random toolbox, only grab the randint tool
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  
            self.dice.append(randint(1,6))   #1 to 6 inclusive

    def get_dice(self): #returns the dice rolls
        return self.dice

# allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  #to show inheritance of Player, add that class to the () like you would a variable
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

