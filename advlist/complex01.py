#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    #print 2nd item in list
    print(list1[1])

    #create a 2nd lists called list2
    list2 = ["juniper"]

    #combine list1 and list2
    list1.extend(list2)

    print(list1)

    #create a 3rd list and call it list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    #append list3 to list1
    list1.append(list3)

    print(list1)

    #print the 5th item in the list1
    print(list1[4])
    
    #print the 1st IP address in list1
    #the IP address is part of another list, so need to get the index where the list starts, and then get the first item
    print(list1[4][0])




main()

