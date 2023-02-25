#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

import crayons

def commandpush(devicecmd): #devicecmd is dict

    for ip in devicecmd.keys():
        print(f'{crayons.green("Handshaking")}. .. ... connecting with {ip}')   #code that connects to device
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}') #code that sends cmds to device
    return None

def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher") 

   # print(commandpush(devicecmd))

    commandpush(devicecmd) # call function to push commands to devices

    #print(devicereboot(devicecmd))

    devicereboot(devicecmd)


def devicereboot(devicecmd):
    for ip in devicecmd.keys():
        print(f"Connecting to... {ip}") #connecting to
        for mycmds in devicecmd[ip]:
            print(f"REBOOTING NOW!... {mycmds}")
    return None

main()

