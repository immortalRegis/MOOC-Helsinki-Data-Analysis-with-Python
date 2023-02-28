#!/usr/bin/env python3


def extract_numbers(s):
    new_s = s
    new_s = new_s.split()
    valid = []
    for sq in new_s:
        try:
            val = int(sq)
            valid.append(val)
        except:
            try:
                val = float(sq)
                valid.append(val)
            except ValueError:
                continue
    return valid
def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
