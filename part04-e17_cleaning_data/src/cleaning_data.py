#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv('src/presidents.tsv', sep='\t')
    df['President'][2] = 'George Bush'
    df['President'][3] = 'Bill Clinton'
    df['Start'][0] = df['Start'][0].split()[0]
    df['Seasons'][3] = 2
    df['Vice-president'][2] = 'Dick Cheney'
    df['Vice-president'][3] = 'Al Gore'
    df['Vice-president'] = (df['Vice-president'].apply(lambda x: (str(x).split()[0].capitalize()) + ' ' + (str(x).split()[1].capitalize())))
    df['Last']  = pd.to_numeric(df['Last'], errors='coerce')
    df = df.astype({'President':object, 'Start':int, 'Seasons':int, 'Vice-president':object})
    return df

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
