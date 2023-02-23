#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across range() to generate n UUIDs"""

import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

#range is required because cant iterate across an integer
#range transforms the integer into an iterable
for rando in range(howmany):
    print( uuid.uuid4() )   # each time through the loop produce a UUID
