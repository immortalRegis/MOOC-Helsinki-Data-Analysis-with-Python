#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)

    x1 = float(((-b) + math.sqrt((b*b) - (4*a*c)))/(2.0*a))
    x2 = float(((-b) - math.sqrt((b*b) - (4*a*c)))/(2.0*a))

    return (x1,x2)


def main():
    print(solve_quadratic(1.047415,6.137105,8.853364))

if __name__ == "__main__":
    main()
