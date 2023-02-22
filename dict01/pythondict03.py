"""Understanding dictionaries
   {key: value, key:value, ...}
   using dict.keys() and dict.values()"""

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
    print( switch.get("version") ) 


    input("Hit return to continue...")
    print("Fourth test - .get()")
    print(switch.keys())  #returns all key in the dictionary

    input("Hit return to continue...")
    print("Fifth test - .get()")
    print(switch.values())  #returns all values in the dictionary



if __name__ == "__main__":
    main()

