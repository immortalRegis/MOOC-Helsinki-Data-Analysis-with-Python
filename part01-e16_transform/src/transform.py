#!/usr/bin/env python3

def transform(s1, s2):
    s1 = s1.split()
    s2 = s2.split()

    l1 = list(map(int, s1))
    l2 = list(map(int, s2))

    return [m1 * m2 for (m1, m2) in zip(l1, l2)]

def main():
    pass

if __name__ == "__main__":
    main()
