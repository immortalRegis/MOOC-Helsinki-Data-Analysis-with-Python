#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    df = df.loc['Akaa':'Äänekoski']
    total_municipalites = df.shape[0]
    growing_df = df[df["Population change from the previous year, %"] > 0]
    total_growing = growing_df.shape[0]
    return (total_growing/total_municipalites)

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col='Region 2018')
    print(f'Proportion of growing municipalities: {100*growing_municipalities(df):.1f}%')

if __name__ == "__main__":
    main()
