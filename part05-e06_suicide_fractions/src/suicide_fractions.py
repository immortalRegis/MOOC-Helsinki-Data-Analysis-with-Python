#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv(r'src/who_suicide_statistics.csv')
    df['suicide_frac'] = df['suicides_no']/df['population']
    mean_values = df.groupby('country').mean()
    return mean_values['suicide_frac']

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
