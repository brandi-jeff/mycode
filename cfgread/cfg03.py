#!/usr/bin/env python3

count = 0
with open("vlanconfig.cfg", "r") as configfile:
    for line in configfile:
        count += 1
#configlist = configfile.readlines()
#print(configlist)
print("The number of lines in this file is: ", count)

