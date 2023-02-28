#!/usr/bin/env python3

import numpy as np

#recommended solution- return np.split(a, a.shape[0], axis=0)
def get_row_vectors(a):
    row_values = [row[np.newaxis, :] for row in a]
    return row_values

#recommended solution - return np.split(a, a.shape[1], axis=1)
def get_column_vectors(a):
    holder = []
    r, c = a.shape
    for i in range(c):
        val = a[:, i]
        holder.append(val[:, np.newaxis])
    return holder

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
