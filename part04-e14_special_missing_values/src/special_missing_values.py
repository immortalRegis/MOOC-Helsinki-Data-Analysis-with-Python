#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep= '\t')
    df.loc[(df['LW'] == 'New') | (df['LW'] == 'Re'), 'LW'] = None
    df = df.dropna(how='any')
    df = df.astype({'LW':'int64'})
    return df[df['Pos'] > df['LW']]

def main():
    special_missing_values()

if __name__ == "__main__":
    main()
