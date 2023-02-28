#!/usr/bin/env python3

import numpy as np
'''the actual solution without loops is 
    a=np.arange(n)
    return a[:, np.newaxis] * a[np.newaxis, :]'''
def multiplication_table(n):
    first = np.arange(0,n)
    
    holder = []
    
    i = 0
    while i < n:
        holder.append(i*first)
        i += 1
    
    values = np.array(holder).reshape(n, n)
    return values

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
