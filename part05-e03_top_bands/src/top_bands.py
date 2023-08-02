#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv(r'src/bands.tsv', sep = '\t')

    top40 = pd.read_csv(r'src/UK-top40-1964-1-2.tsv',sep = '\t')
    bands['Band'] = bands['Band'].str.upper()
    
    return pd.merge(bands, top40, left_on=['Band'], right_on=['Artist']).sort_values('Pos')

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
