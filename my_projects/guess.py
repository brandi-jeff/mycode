#!/usr/bin/env python3

#rules.. unscrample the word

import secrets
import random

def main():
    #Have list for answers
    answer = ["mammoth", "pencil", "mystery", "silent", "throw", "garden"]
    
    #need to choose a word to scramble randomly and store
    rand = secrets.choice(answer)
    rand_list = list(rand)
    #then scramble chosen word and store
    random.shuffle(rand_list)
    scrambled = ''.join(rand_list)
    #print scrambled word for user to see
    print(scrambled)
        #get user input
        #give certain number of chances.. while loop
        #match user input to actual word

  
#    if guess == answer[]

# word = random.choice(answer)
# letters_list = word.split("")
# 


if __name__ == "__main__":
    main()
