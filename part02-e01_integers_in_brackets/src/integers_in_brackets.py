#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    criterion = re.compile(r'\[\s*([+-]?\d*)\s*\]')
    answers = criterion.findall(s)
    
    return (list(map(int, answers)))


def main():
    integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")

if __name__ == "__main__":
    main()
