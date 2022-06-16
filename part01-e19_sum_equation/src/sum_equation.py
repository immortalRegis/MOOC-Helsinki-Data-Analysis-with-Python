#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return '0 = 0'
    NL = L.copy()
    NL = list(map(str, NL))
    total = sum(L)
    return  f'{" + ".join(NL)} = {total}'

def main():
    pass

if __name__ == "__main__":
    main()
