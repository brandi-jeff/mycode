#!/usr/bin/python3
"""Exploring using pandas to create dataframes, and output graphs"""

#typically aliased as pd
import pandas as pd

def main():
    excel_file = 'movies.xls'

    #create a DataFrame (DF) object.
    movies = pd.read_excel(excel_file)

    #.head() will print 1st 5 rows by default
    print(movies.head())

    #read excel sheet, look at 1st sheet and 1st column in that sheet
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    print(movies_sheet1.head())

    #export 5 movies from the top dataframe to excel
    movies_sheet1.head().to_excel("5movies.xlsx")

    #export 5 movies from the top of the dataframe to json
    movies_sheet1.head().to_json("5movies.json")

    #export 5 movies from the top of the dataframe to csv
    movies_sheet1.head().to_csv("5movies.csv")


if __name__ == "__main__":
    main()

