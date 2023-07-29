#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    
    index = pd.Index(np.arange(1, len(df) + 1, 1), name='LW')
    

    df['LW'] = df['LW'].replace(to_replace=['New', 'Re'], value= np.nan)
    df = df.dropna(how='any')
    df['LW'] = pd.to_numeric(df['LW'], downcast='integer')
    df['WoC'] = df['WoC'] - 1 #reduce number of weeks on chart
    
    df = df.set_index('LW').reindex(index).reset_index() #use this line to introduce np.nan values to missing chart positions
    df['Peak Pos'] = np.where((df['Peak Pos'] == df['Pos']) & (df['LW'] > df['Peak Pos']), np.nan, df['Peak Pos'])
    # If the current weeks position is the same as peak position but last weeks position is lower then assume the song peaked this
    # week and set last week's peak position to np.nan

    df['Pos'] = df['LW']
    df['LW'] = np.nan
    
    
    return df.sort_values(by='LW')

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
