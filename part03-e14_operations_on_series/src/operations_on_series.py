#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index= ['a', 'b', 'c'])
    s2 = pd.Series(L2, index= ['a', 'b', 'c'])
    return (s1, s2)
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    
    return (s1, s2.drop(labels = ['b'])) #we can also use del s2["b"]
    
def main():
    s1, s2 = create_series([1, 3, 5], [2, 4, 6])
    s3, s4 = modify_series(s1, s2)
    print(s3 + s4)
    
if __name__ == "__main__":
    main()
