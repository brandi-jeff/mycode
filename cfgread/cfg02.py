#!/usr/bin/env python3
'''Working with reading from files using splitlines()'''

configfile = open("vlanconfig.cfg", "r")

configblog = configfile.read()

#strips out \n
configlist = configblog.splitlines()
print(configlist)
configfile.close()

