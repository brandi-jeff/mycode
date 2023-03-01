#!/usr/bin/env python3
'''Testing JSON'''

import requests

TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"

def main():
    #PART A
    #pull a time object from date.jsontest.com and make the request
    #strip json
    mytime = requests.get(TIMEURL).json()
    
    #pull out the value associated with the KEY "time" then strip out all whitespaces then replace colons with hyphens
    mytime = mytime["time"].replace(" ", "").replace(":", "-")

    #PART B
    #make the request, strip json
    myip = requests.get(IPURL).json()
    print(myip)
    
    #grab the value associated with the KEY "ip"
    myip = myip["ip"]

    #PART C
    #read text file
    with open("/home/student/mycode/jsontest/myservers.txt") as myfile:
        mysvrs = myfile.readlines()

    #PART D
    #test data to validate as legal json
    jsonToTest = {}
    jsonToTest["time"] = mytime
    jsonToTest["ip"] = myip
    jsonToTest["mysvrs"] = mysvrs

    ''' when a POST json= is replaced by the KEY "json",  the key "json" is mapped to a VALUE of the json to test
    this is because the test item is a string, we can include whitespaces. Format for requests to validate.testjson.com is... 
    data={"json": "json you want to validate as str"} '''
    mydata = {}
    mydata["json"] = str(jsonToTest)

    #PART E
    #use requests library to send an HTTP POST
    resp = requests.post(VALIDURL, data=mydata).json()

    print(resp)
    print(f"Is your JSON valid? {resp['validate']}")



if __name__ == "__main__":
    main()
