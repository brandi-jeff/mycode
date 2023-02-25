#!/usr/bin/env python3

'''read the file'''
#with open("dracula.txt", "r") as vampfile:
 #   reading = vampfile.readlines()
#print(reading)

''' loop over file and print each line'''
#with open("dracula.txt", "r") as vampfile:
#    for line in vampfile:
#        print(line)

''' lopp over file and only print lines with word vampire and find the word with any case'''
#with open("dracula.txt", "r") as vampfile:
#    for line in vampfile:
#        if "vampire" in line.lower():
#            print(line)

'''print how many lines containe the word vampire'''
#vamplines = 0
#with open("dracula.txt", "r") as vampfile:
#    for line in vampfile:
#        if "vampire" in line.lower():
#            print(line)
#            vamplines += 1
#    print(vamplines)

'''write lines with vampire to a new file'''
vamplines = 0
with open("dracula.txt", "r") as vampfile:
    with open ("vampiretimes.txt", "w") as vampcount:
        for line in vampfile:
            if "vampire" in line.lower():
                print(line)
                vamplines += 1
                vampcount.write(line)

print(vamplines)
