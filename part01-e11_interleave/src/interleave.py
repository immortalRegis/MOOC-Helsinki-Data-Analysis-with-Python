#!/usr/bin/env python3

def interleave(*lists):
    holder = zip(*lists)
    new_holder = []
    for thing in holder:
        new_holder.extend(thing)
    
    return new_holder
    

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
