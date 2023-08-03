#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv(r'src/who_suicide_statistics.csv')
    df['suicide_frac'] = df['suicides_no']/df['population']
    mean_values = df.groupby('country').mean()
    return mean_values['suicide_frac']
    
def suicide_weather():    
    wf=pd.read_html(r"src/List_of_countries_by_average_yearly_temperature.html" , index_col="Country",header=0)
    
    temp = wf[0]['Average yearly temperature (1961–1990, degrees Celsius)']
    temp = temp.replace(to_replace="\u2212", value="-", regex=True)

    temp_series = pd.to_numeric(temp, downcast = 'signed')
    suicide_series = suicide_fractions()

    suicide_rows = len(suicide_series)
    temp_rows = len(temp_series)

    common_series = pd.merge(suicide_series, temp_series, left_on = 'country', right_on = 'Country')
    common_rows = len(common_series)

    corr_val = suicide_series.corr(temp_series, method = 'spearman')
    
    return (suicide_rows, temp_rows, common_rows, corr_val)
    
    

def main():
    sui_rows, tem_rows, com_rows, cor_val = suicide_weather()
    print(f'Suicide DataFrame has {sui_rows} rows Temperature DataFrame has {tem_rows} rows Common DataFrame has {com_rows} rows Spearman correlation: {cor_val:.1f}')

if __name__ == "__main__":
    main()
