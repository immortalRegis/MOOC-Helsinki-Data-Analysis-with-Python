#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            product = i * j
            print('{:4d}'.format(product), end='')
        print()
            

if __name__ == "__main__":
    main()
