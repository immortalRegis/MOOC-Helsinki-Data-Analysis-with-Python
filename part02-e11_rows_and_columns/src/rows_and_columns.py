#!/usr/bin/env python3

import numpy as np
#After submission, I saw that you could solve the problem using list comprehension [row for row in a]
# [row for row in a.T]. Not bad at all

def get_rows(a):
    holder = []
    #recall that the .shape call returns a tuple (no. of rows, no. of columns) if you have multiple rows
    
    for i in range(a.shape[0]):
        holder.append(a[i])
    return holder

def get_columns(a):
    holder = []
    values = a.T
    for i in range(values.shape[0]):
        holder.append(np.array(values[i]))
    return holder

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
