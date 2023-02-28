#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_red(pic):
    red_pic = pic.copy()
    red_pic[:, :, 1:] = 0
    return red_pic

def to_green(pic):
    green_pic = pic.copy()
    green_pic[:, :, [0, 2]] = 0
    return green_pic

def to_blue(pic):
    blue_pic = pic.copy()
    blue_pic[:, :, :2] = 0
    return blue_pic

def to_grayscale(pic):
    gray_pic = pic.copy()
    gray_values = np.dot(pic[:, :, :], [0.2126, 0.7152, 0.0722])
    return gray_values
    

def main():
    pic = r"src/painting.png" 
    picture = plt.imread(pic)    
    
    gr_p = to_grayscale(picture)
    plt.imshow(gr_p)
    
    rp = to_red(picture)
    gp = to_green(picture)
    bp = to_blue(picture)

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(rp)
    ax[1].imshow(gp)
    ax[2].imshow(bp)
    plt.show()


    

    

if __name__ == "__main__":
    main()
