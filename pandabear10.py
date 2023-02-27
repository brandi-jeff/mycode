#!/usr/bin/python3
"""In pandas, a single point in time is represented as a Timestamp. We can use the to_datetime() function to create Timestamps from strings in a wide variety of date/time formats. Let’s import pandas and convert a few dates and times to Timestamps.
"""

import pandas as pd

def main():
    #infers date based on input, switches time to 24h format
    print(pd.to_datetime("2023-02-28 4:06pm"))

    #will print with month first in format YY-MM-DD
    print(pd.to_datetime("6/3/1975"))

    #will print with day first in format YY-DD-MM
    print(pd.to_datetime("6/3/1975", dayfirst=True))
    
    #will give datetime index
    print(pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995']))

    #can specify format that the data is being input so python doesn't assume it default format
    print(pd.to_datetime(['4/25/17', '8/15/20', '12/15/12'], format='%m/%d/%y'))

if __name__ == "__main__":
    main()
