#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    ndf = df

    full_date = ndf['Päivämäärä']
    
    day_dict = {'ma':'Mon','ti':'Tue','ke':'Wed','to':'Thu','pe':'Fri','la':'Sat','su':'Sun'}
    month_dict = {'tammi':1,'helmi':2,'maalis':3,'huhti':4,'touko':5,'kesä':6,'heinä':7,'elo':8,'syys':9,'loka':10,'marras':11,'joulu':12}

    full_date = full_date.dropna()
    expanded_date = full_date.str.split(expand=True)
    expanded_date[0] = expanded_date[0].map(day_dict)
    expanded_date[2] = expanded_date[2].map(month_dict)

    split_time = expanded_date[4].str.split(':')
    hours = split_time.apply(lambda x: x[0])
    expanded_date[4] = hours
    expanded_date = expanded_date.rename(columns={0:'Weekday', 1:'Day', 2:'Month', 3:'Year', 4:'Hour'})
    return expanded_date.astype({'Weekday':str, 'Day':int, 'Month':int,'Year':int, 'Hour':int})

def cycling_weather():
    cycle2 = pd.read_csv(r'src/kumpula-weather-2017.csv')
    cycle2 = cycle2.drop(columns = ['Time', 'Time zone'])
    cycle = cycle2.rename(columns = {'m':'Month', 'd':'Day'})
    
    df = pd.read_csv(r'src/Helsingin_pyorailijamaarat.csv', sep=';')
    
    split_weather = split_date(df)
    df = df.drop(columns = ['Päivämäärä'])
    df = df.dropna(how = 'all', axis = 1)
    
    
    weather = pd.concat([split_weather, df], axis = 1)
    print(weather)
    
    
    merge_keys = ['Day', 'Month', 'Year']
    return pd.merge(cycle, weather, left_on = merge_keys, right_on = merge_keys)

def main():
    print(cycling_weather())

if __name__ == "__main__":
    main()
