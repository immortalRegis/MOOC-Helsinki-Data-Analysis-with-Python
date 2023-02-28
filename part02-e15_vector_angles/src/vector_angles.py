#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    x_norm = np.sqrt(np.sum(X**2, axis=1))
    y_norm = np.sqrt(np.sum(Y**2, axis=1))
    
    dot_prod = np.sum(X*Y, axis=1)

    value = dot_prod/(x_norm*y_norm)
    
    new_values = np.clip(value, -1, 1)

    return(np.degrees(np.arccos(new_values)))
    #np.array([])

def main():
    X= np.array([[0, 0, 1], [-1, 1, 0]])
    Y = np.array([[0, 1, 0], [1, 1, 0]])
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
