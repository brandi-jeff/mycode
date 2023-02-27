#!/usr/bin/python3
'''using pandas to '''

import pandas as pd

def main():

    ## create a python list
    mydata = [
    {'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'},
    {'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'}
    ]

    #make data frame from list
    df = pd.DataFrame(mydata)

    #create csv file without index
    df.to_csv("inventorypandas.csv", index=False)



if __name__ == "__main__":
    main()
