#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    coeff_mat = np.array([[-a1, -b1, 1],[-a2, -b2, 1], [-a3, -b3, 1]])
    cons_mat = np.array([[c1],[c2],[c3]])
    answers = np.linalg.solve(coeff_mat, cons_mat)
    
    return (answers[1, 0], answers[0, 0], answers[2,0])
    # I used this return form because the method kept returning the tuple (y, x, z)
    # It turns out the problem was from my coefficient matrix
    # I went with (-y, -x, cons) forgeting that b = x and a = y.

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
