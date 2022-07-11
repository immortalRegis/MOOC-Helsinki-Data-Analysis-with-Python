#!/usr/bin/env python3

import sys

def file_count(filename):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(filename, 'r') as lines:
        for line in lines:
            char_count += len(line)
            words = line.split()
            word_count += len(words)
                            

            line_count +=1

    return (line_count, word_count, char_count)

def main():
    holder = sys.argv[1:]
    for hd in holder:
        values = file_count(hd)
        print(f'{values[0]}\t{values[1]}\t{values[2]}\t{hd}')

if __name__ == "__main__":
    main()
