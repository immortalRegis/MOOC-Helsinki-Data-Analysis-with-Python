#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv(r'src/UK-top40-1964-1-2.tsv', sep='\t')
    company = df.groupby('Publisher').sum().drop(columns=['Pos','Peak Pos'])
    company = company.sort_values('WoC', ascending = False).reset_index()
    best_company = company.loc[0]['Publisher']
    mask = df['Publisher'] == best_company
    return df[mask]
    

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
