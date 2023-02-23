#!/usr/bin/env python3

#name of the import matches the file name (minus .py)
#must be in the same directory
import first_module   
#when this program is run, this import will change the name from __main__ to the name of the file being imported 


first_module.main()


#this sets the name to __main__ because it is the file being run directly by Python
print("Module #2 Name=", __name__)

