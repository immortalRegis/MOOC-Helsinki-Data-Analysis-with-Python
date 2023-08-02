#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date(df):
    ldf = df
    full_date = ldf['Päivämäärä']
    
    day_dict = {'ma':'Mon','ti':'Tue','ke':'Wed','to':'Thu','pe':'Fri','la':'Sat','su':'Sun'}
    month_dict = {'tammi':1,'helmi':2,'maalis':3,'huhti':4,'touko':5,'kesä':6,'heinä':7,'elo':8,'syys':9,'loka':10,'marras':11,'joulu':12}

    expanded_date = full_date.str.split(expand=True)
    expanded_date[0] = expanded_date[0].map(day_dict)
    expanded_date[2] = expanded_date[2].map(month_dict)

    split_time = expanded_date[4].str.split(':')
    hours = split_time.apply(lambda x: x[0])
    expanded_date[4] = hours
    expanded_date = expanded_date.rename(columns={0:'Weekday', 1:'Day', 2:'Month', 3:'Year', 4:'Hour'})
    expanded_date.astype({'Weekday':str, 'Day':int, 'Month':int,'Year':int, 'Hour':int})
    
    df = df.drop(columns = 'Päivämäärä')
    df = df.dropna(how='all', axis = 1)


    return pd.concat([expanded_date, df], axis = 1)
    
def cyclists_per_day():
    df = pd.read_csv(r'src/Helsingin_pyorailijamaarat.csv', sep= ';')
    df = df.dropna(how='all')
    df = split_date(df)
    return df.groupby(['Year', 'Month', 'Day']).sum()
    
    
def main():
    df = cyclists_per_day()
    
    august_2017 = df.loc['2017',8]
    plt.plot(august_2017)
    plt.show()
    

if __name__ == "__main__":
    main()
