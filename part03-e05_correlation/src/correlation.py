#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    holder = load()
    sepal_len = []
    petal_len = []
    
    for val in holder:
        sepal_len.append(val[0])
        petal_len.append(val[2])
        
    return scipy.stats.pearsonr(sepal_len, petal_len)[0]
    #Recommended solution!! I could have just used multi-dimensional array referencing
    # iris = load()
    #result = scipy.stats.pearsonr(iris[:,0], iris[:,2])
    
def correlations():
    holder = load()
    sepal_len = []
    sepal_wid = []
    petal_len = []
    petal_wid = []
    
    for val in holder:
        sepal_len.append(val[0])
        sepal_wid.append(val[1])
        petal_len.append(val[2])
        petal_wid.append(val[3])

    return np.array(np.corrcoef([sepal_len, sepal_wid, petal_len, petal_wid]))
    # Recommended solution. Lesson learnt: I could have just transposed the matrix using mat.T
    #iris = load()
    #temp = iris.T
    #return np.corrcoef(temp)

def main():
    print(correlations())
    print(lengths())

if __name__ == "__main__":
    main()
