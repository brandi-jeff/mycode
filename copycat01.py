#!/usr/bin/env python3

import shutil #allows for higher-level file manipulation
import os #allows for os manipulation

#tells program to start in this specific directory no matter where its run from on the system
os.chdir("/home/student/mycode/")

#this copies the file path source(fileA) to the file (fileB) at the path destination
#returns a string of the path of the copied filed
              #fileA                         fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copies the folder at the path source and its files/subfolders(DirectoryA)  to destination directory (DirectoryB)
                 #DirectoryA        #DirectoryB
shutil.copytree("5g_research/", "5g_research_backup/")


