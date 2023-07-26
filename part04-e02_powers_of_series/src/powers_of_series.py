#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    holder = []
    for i in range(1, k + 1):
        holder.append(s**i)

    ind = list(s.index)
    cols = np.arange(1, k +1)

    df = pd.DataFrame(holder).T
    df.columns = cols
    df.index = ind
    

# recommended solution 
#   c=[ s**i for i in range(1,k+1) ]
#   df = pd.DataFrame(dict(zip(range(1,k+1), c)))
    return df
    
def main():
    s1 = pd.Series([1, 2, 3])
    print(powers_of_series(s1, 4))
    
if __name__ == "__main__":
    main()
