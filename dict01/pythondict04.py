"""Understanding dictionaries
   {key: value, key:value, ...}
   using the del keyword with a dict
   adding and removing values from the dict"""

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch)

    ## proove that switch is indeed a dictionary
    print(type(switch))

    ## display parts of the dictionary
    print( switch["hostname"] )    # displays "sw1"
    print( switch["ip"] )          # displays "10.0.1.1"

    input("Hit return to continue...")
    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get("lynx") ) # alternative to switch["lynx"]
    #print(switch.get("lynx", None)) # this is what is actually being run...
                                     # by default dict.get() returns "None"

    input("Hit return to continue...")
    # if you want to customize what is returned when the key is not found
    print( "Second test - .get()" )
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )
    
    input("Hit return to continue...")
    print( "Third test - .get()" )
    print( switch.get("version") ) # alternative to switch['version']
                                   # this key exists, so it will return a value of "1.2"
    input("Hit return to continue...")
    # this returns all of the keys in the dictionary
    print( "Fourth test - .keys()" )
    print( switch.keys() )    # dict.keys() returns all the keys in a "list like" structure

    input("Hit return to continue...")
    # return all of the values in the dictionary
    print( "Fifth test - .values()" )
    print( switch.values() )

    del switch["vendor"]

    input("Hit return to continue...")
    print("Seventh test - .pop()")
    print(switch.pop("version"))
    print(switch.keys())
    print(switch.values())


    input("Hit return to continue...")
    print( "Eighth test - ADD a new value" )
    switch["adminlogin"] = "karl08"
    print( switch.keys() )
    print( switch.values() )

    input("Hit return to continue...")
    print( "Ninth test - ADD a new value" )
    switch["password"] = "qwerty"
    print( switch.keys() )
    print( switch.values() )

    input("Hit return to continue...")
    print(list(switch.values())[2])






if __name__ == "__main__":
    main()
