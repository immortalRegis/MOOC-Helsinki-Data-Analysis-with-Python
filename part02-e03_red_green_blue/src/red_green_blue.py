#!/usr/bin/env python3
import re
#I used the convoluted process because I couldn't figure out the
#regex for the second part of the re.search pattern. The regex is (.*)\n
def red_green_blue(filename="src/rgb.txt"):
    holder = []
    with open(filename, 'r') as lines:
        for line in lines:
            m = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s", line)
            if m:
                t = list(m.groups())
                ln = line.split()
                if len(ln) == 4:
                    t.append(ln[3])
                else:
                    word = ln[3] + ' ' + ln[4]
                    t.append(word)
                k = '\t'.join(t)
                holder.append(k)
                 
    return holder


def main():
    chalet = red_green_blue()
    print(chalet)

if __name__ == "__main__":
    main()
