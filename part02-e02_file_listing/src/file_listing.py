#!/usr/bin/env python3

import re

def file_listing(filename="src/listing.txt"):
    holder = []
    nums = re.compile(r"(\d+)")
    months = re.compile(r"Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec")
    
    with open(filename, 'r') as contents:
        for line in contents:
            numbers = nums.findall(line)
            numbers = list(map(int, numbers))
            size = numbers[1]
            day = numbers[2]
            hour = numbers[3]
            minute = numbers[4]

            mo = months.findall(line)
            month = mo[0]

            line = line.split()
            file_name = line[-1]
            current_record = (size, month, day, hour, minute, file_name)
            holder.append(current_record)

    return holder            

def main():
    pass

if __name__ == "__main__":
    main()
