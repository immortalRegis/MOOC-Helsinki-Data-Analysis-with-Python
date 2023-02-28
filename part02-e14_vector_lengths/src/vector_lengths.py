#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    a2 = a**2
    row_sums = a2.sum(axis=1)
    norms = np.sqrt(row_sums)
    return np.array(norms)

def main():
    np.random.seed(0)
    a = np.random.randint(0, 11, (3, 4))
    print(vector_lengths(a))

if __name__ == "__main__":
    main()
