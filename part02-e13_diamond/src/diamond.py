#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n == 1:
        return np.eye(1)
    holder = []

    iden_mat = np.eye(n, dtype= int)
    
    # To create the top of the diamond, attach the reverse of each row from index 1 to the end to the front
    # of each row 
    for row in iden_mat:
        ex = row[1:]
        holder.append(np.concatenate((ex[::-1], row)))
    
    #To create the bottom of the diamond, from index n-1 to 0, attach each row to the end of the list 'holder'
    temp_holder = holder[::-1]
    for i in range(1, len(temp_holder)):
        holder.append(temp_holder[i])

    
    return np.array(holder)

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
