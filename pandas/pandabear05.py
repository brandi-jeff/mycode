import pandas as pd
import pprint

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    #export to json and dont include index
    ciscodf.to_json("combined_ciscodata.json", orient="records")

    #export to csv and dont include index
    ciscodf.to_csv("combined_ciscodata.csv", index=False)

    #export to excel and dont include index
    ciscodf.to_excel("combined_ciscodata.xls", index=False)
    #xlsx is default format from 2007 and later
    ciscodf.to_excel("combined_ciscodata.xlsx", index=False)

    #create python dictionary without index number
    x = ciscodf.to_dict(orient='records')
    pprint.pp(x)

if __name__ == "__main__":
    main()
