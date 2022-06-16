#!/usr/bin/env python3

def find_matching(L, pattern):
    indices = []

    for i, word in enumerate(L):
        if pattern in word:
            indices.append(i)
    
    return indices

def main():
    pass

if __name__ == "__main__":
    main()
