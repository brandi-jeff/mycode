#!/usr/bin/python3

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    print(ciscodf)

    print()

    #export to json
    ciscodf.to_json("combined_ciscodata.json")

    #export to csv
    ciscodf.to_csv("combined_ciscodata.csv")

    #export to excel
    ciscodf.to_excel("combined_ciscodata.xls")

    #create python dictionary
    x = ciscodf.to_dict()
    print(x)

if __name__ == "__main__":
    main()
