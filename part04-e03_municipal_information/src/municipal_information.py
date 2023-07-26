#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv(r"src/municipal.tsv", sep=r'\t')
    rows, columns = df.shape
    print(f"Shape: {rows},{columns}")
    print("Columns:")
    for name in df.columns:
        print(name.strip('\"'))


if __name__ == "__main__":
    main()
