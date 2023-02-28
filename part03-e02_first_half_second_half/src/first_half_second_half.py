#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    col = a.shape[1]
    half_col = col//2

    c = np.sum(a[:, :half_col], axis=1) > np.sum(a[:, half_col:], axis = 1)
    return np.array(a[c])

def main():
    a = np.array([[1, 3, 4, 2],[2, 2, 1, 2]])
    print(first_half_second_half(a))
    

if __name__ == "__main__":
    main()
