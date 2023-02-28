#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
 
def subfigures(a):
    fg, ax = plt.subplots(1,2)
    x = a[:, 0]
    y = a[:, 1]

    
    colors = a[:, 2]
    size = a[:, 3]
 
    ax[0].plot(x, y)
    ax[1].scatter(x, y, c= colors, s = size)
    plt.show()
    
 
 
    
 
def main():
   a = np.array([[0,1,2,3,4],[5, 6, 7, 8,9,]])
   subfigures(a)
   
 
if __name__ == "__main__":
    main()