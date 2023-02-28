#!/usr/bin/env python3

import numpy as np
from functools import reduce
def matrix_power(a, n):
    holder = []
    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    if n == 1:
        return a
    if n > 1:
        for i in range(n):
            holder.append(a)
    else: # using the laws of indices, express -n as (-1) * n
        b = np.linalg.inv(a)
        n = -n
        for i in range(n):
            holder.append(b)

    return (reduce(lambda a, b: a@b, holder))

def main():
    a = np.array([[1, 2], [3, 4]])
    print(matrix_power(a, -1))

if __name__ == "__main__":
    main()
