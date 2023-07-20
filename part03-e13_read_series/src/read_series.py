#!/usr/bin/env python3
import pandas as pd

def read_series():
    index_holder = []
    value_holder = []

    while(True):
        entry = input("Enter the values separated by space")
        if len(entry.strip()) == 0:
            break
        contents = entry.split()
        
        if len(contents) != 2:
            raise ValueError('Incorrect values.')
        index, value = contents

        index_holder.append(index)
        value_holder.append(value)

        

    return pd.Series(value_holder, index = index_holder)

def main():
    print(read_series())

if __name__ == "__main__":
    main()
