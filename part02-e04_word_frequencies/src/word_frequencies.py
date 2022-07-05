#!/usr/bin/env python3
def word_frequencies(filename):
    holder = {}
    with open(filename, 'r') as lines:
        for line in lines:
            line = line.split()

            for word in line:
                word = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                if not word in holder.keys():
                    holder[word] = 1
                else:
                    word_count = holder[word]
                    word_count += 1
                    holder[word] = word_count
    return holder

def main():
    counter = word_frequencies('C:/Users/user/AppData/Local/tmc/vscode/mooc-data-analysis-with-python-2021/part02-e04_word_frequencies/src/alice.txt')
    for k, v in counter.items():
        print(f'{k}\t{v}')

if __name__ == "__main__":
    main()
