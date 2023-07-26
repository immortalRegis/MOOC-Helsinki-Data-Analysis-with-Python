#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    indices = s.index
    values = s.values

    return pd.Series(indices, index = values)

def main():
    test_series = pd.Series([1, 2,3, 1], index = ['w', 'x','y','z'])
    print(test_series)
    print(inverse_series(test_series))

if __name__ == "__main__":
    main()
