#!/usr/bin/env python3
'''create a dataframe from a timeseries dataset'''

import pandas as pd

def main():
    opsd_daily = pd.read_csv('netTraffic.csv')
    print(opsd_daily.shape)

    print(opsd_daily.head(3))
    print(opsd_daily.tail(3))

    print(opsd_daily.dtypes)
    
    #reassign so 1st index is the date
    opsd_daily = opsd_daily.set_index('Date')
    input("Press enter to continue..")

    print("\nLook at the first three rows after date has been set as the primary index")
    print(opsd_daily.head(3))

    print("\nLook at the last three rows after date has been set as the primary index")
    print(opsd_daily.tail(3))

    #will display all index values 
    input("\nPress ENTER to look at all of the index values associated with the dataset (dates)")
    print(opsd_daily.index)

    #consolidate the above steps into a single line using the index_col and parse_dates parameters of the read_csv() function
    opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)

    #can add cols
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    #prints random sample of the data. random_state=0 means every time this is run, the same info will be spit out
    input("\nPress ENTER to look at a random sampling from 5 rows after adding the Year, Month and Weekday Name columns")
    print(opsd_daily.sample(5, random_state=0))


if __name__ == "__main__":
    main()
