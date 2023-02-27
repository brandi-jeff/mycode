#!/usr/bin/env python3

'''Practicing ranges'''
import time

'''TO DO: dont allow user to put more than 10 beers'''

def main():
    beers_start = int(input("How many bottles of beer? "))
   # print(f"{str(beers_start)} bottles of beer on the wall!")

    for beer in range(beers_start, 1, -1):
        print(f"{str(beer)} bottles of beer on the wall!\n{str(beer)} bottles of beer on the wall! {str(beer)} bottles of beer. Take one down, pass it around.")
        time.sleep(1)
    print("1 bottle of beer on the wall!")

if __name__ == "__main__":
    main()
