#!/usr/bin/env python3

def reverse_dictionary(d):
    holder = {}
    for k, v in d.items():
        for word in v:
            if word not in holder.keys():
                holder[word] = []           
            holder[word].append(k)
    
    return holder

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    for k, v in d.items():
        print(f'{k}: {v}')
    
    h = reverse_dictionary(d)
    for k, v in h.items():
        print(f'{k}:{v}')
    

if __name__ == "__main__":
    main()
