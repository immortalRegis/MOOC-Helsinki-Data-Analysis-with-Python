#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv('src/municipal.tsv', sep='\t',index_col='Region 2018')
    mn = df.loc['Akaa':'Äänekoski']
    needed_mn = mn[(mn["Share of Swedish-speakers of the population, %"] > 5) & (mn["Share of foreign citizens of the population, %"] >5)]
    return needed_mn[["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]

def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
