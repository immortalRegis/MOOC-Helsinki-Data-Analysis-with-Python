#!/usr/bin/python3
import numpy as np

def almost_meeting_lines(a1, b1, a2, b2):
    A = np.array([[-a1, 1],[-a2, 1]])
    b = [[b1],[b2]]

    A_rank = np.linalg.matrix_rank(A)
    exact = False
    if (A_rank == A.shape[0]) and (A_rank == A.shape[1]):
        exact = True
    
    values = np.linalg.lstsq(A, b)
    x =  values[0][0][0].round()
    y =  values[0][1][0].round()

    print(f'x is {x} and y is {y}')
    return ((x, y), exact)

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
