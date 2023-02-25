#!/usr/bin/env python3

#rules.. unscrample the word

import random

def gameplay():
 
    #Have list for answers
    answer = ["mammoth", "pencil", "mystery", "silent", "throw", "garden"]
    
    #need to choose a word to scramble randomly and store
    rand = random.choice(answer)
    rand_list = list(rand)
   
    #then scramble chosen word and store
    random.shuffle(rand_list)
    scrambled = ''.join(rand_list)
    
    #game starts
    name = input("Great! What is your name? ")
    name = name.capitalize()
    #print scrambled word for user to see
    print(f"Hi {name}! Your word is: " + scrambled)
    
    #give certain number of chances.. while loop
    count = 0
    total = 5
    answer = ""
    while count < 5 and answer != rand:    
        #get user input
        answer = input("Please enter your guess: ")
        if len(answer) != len(rand):
            print(f"Your guess must have {len(rand)} characters.")
        elif answer.lower() == rand:
            print(f"Congratulations {name}! You unscrambled the word!\nThanks for playing! Bye!")
        else:
            count += 1
            chances = str(total - count)
            if chances == "0":
                print(f"Oh no! You ran out of chances. The correct answer was {rand}.\nThanks for playing {name}! Bye!")
            else:
                print("Incorect. You have " + str(chances) + " chance(s) left.")
        #continue 

def main():
    print("Welcome to Unscramble Me! You will have five chances to try to unscramble the given word.")
    play = input("Do you want to play? (Y/n) ")
    if play.lower() != "n":
        gameplay()
    else:
        print("That sucks. Maybe next time. Bye!")

if __name__ == "__main__":
    main()
