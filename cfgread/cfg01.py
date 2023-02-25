#!/usr/bin/env python3


######## EXPLORE READ ##########
## create file object in read mode
configfile = open("vlanconfig.cfg", "r")
print(configfile.read())
configfile.close()


######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

##.readlines() creates a list
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    #remove extar line
    #print(x), end="")
    #.strip() will remove white space and extra line so done need end=""
    print(x.strip())

configfile.close()

