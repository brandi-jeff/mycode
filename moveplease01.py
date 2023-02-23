#!/usr/bin/env python3

import shutil
import os

def main():
    #force program to start at this location
    os.chdir('/home/student/mycode/')

    #syntax shutil.move(source, destination)
    #will return string of absolute path of new location
    #if file name already exists, will be overriden with .move so be careful
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompt user for new file name
    xname = input("What is the new name for kerrigan.obj? ")

    #rename based on input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



main()
