#!/usr/bin/env python3
import sys
import math

def summary(filename):
    sum = 0
    average = 0
    sd = 0
    valid_nums = 0
    holder = []

    with open(filename, 'r') as numbers:
        for num in numbers:
            try:
                value = float(num)
                sum += value
                valid_nums += 1
                holder.append(value)
            except ValueError:
                print('Enter only valid numbers')

        if valid_nums > 0:
            average = sum/valid_nums
            dev_sum = 0
            for nm in holder:
                deviation = nm - average
                dev_square = deviation * deviation
                dev_sum += dev_square

            sd = math.sqrt(dev_sum / (valid_nums - 1))
        
    return (sum, average, sd)

def main():
    needed_files = sys.argv[1:]
    for nf in needed_files:
        values = summary(nf)
        print(f"File: {nf} Sum: {values[0]:.6f} Average: {values[1]:.6f} Stddev: {values[2]:.6f}")

if __name__ == "__main__":
    main()
