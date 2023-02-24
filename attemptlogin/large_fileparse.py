#!/usr/bin/python3


loginfail = 0
loginpass = 0

#use with this time
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            #get ip address of failed attempt
            print("The IP Address of the fialed attempt was: " +  line.split(" ")[-1])
        if "INFO" in line:
            loginpass += 1
print("The number of failed log in attempts is", loginfail)
print("The number of successful log in attempts is", loginpass)
