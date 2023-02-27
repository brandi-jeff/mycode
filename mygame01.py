#!/usr/bin/env python3

'''Using dictionaries to create rpg game'''

def showInstructions():
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]''')

#show player where they are and whats going on
def showStatus():
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

#inventory starts out empty
inventory = []

#dictionary linking one room to other rooms
rooms = {
          'Hall' : {
                  'south' : 'Kitchen',
                  'east' : 'Dining Room',
                  'item' : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                },

            'Bathroom' : {
                  'north' : 'Dining Room',
                  'item' : 'Monster'
                },

            'Dining Room': {
                  'west' : 'Hall',
                  'south' : 'Bathroom',
                  'item' : 'dish'
                }
            }

#start position
currentRoom = 'Kitchen'

showInstructions()

while True:
    showStatus()

    move = ''
    while move == '':
        move = input('>')

    #lowercase input and turn to list using split
    #splits on first space if there are multiple words
    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")


    if move[0] == 'get':
        #is there an item in the room AND is the item they asked for in the room
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' acquired')
            #delete the item key:value pair since it is no longer in the room
            del rooms[currentRoom]['item']
        else:
            print("Can't get " + move[1] + "!")

    if 'item' in rooms[currentRoom] and 'Monster' in rooms[currentRoom]['item']:
        print("A monster has eaten you... GAME OVER!")
        break
