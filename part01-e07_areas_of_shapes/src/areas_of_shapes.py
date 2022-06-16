#!/usr/bin/env python3

import math

def aot(base:int, height:int):
    return float(0.5 * base * height)

def aor(width: int, height: int):
    return float(width * height)

def aoc(radius: int):
    return math.pi * radius * radius

def main():
    # enter you solution here
    while True:
        shape = input('Choose a shape (triangle, rectangle, circle):')
        shape = shape.strip()
        if shape == '':
            break
        elif shape == 'triangle':
            base = int(input('Give base of the triangle: '))
            height = int(input('Give height of the triangle: '))
            area = aot(base, height)
            print(f'The area is {area:.6f}')
        elif shape == 'rectangle':
            width = int(input('Give the width of the rectangle: '))
            height = int(input('Give the height of the rectangle: '))
            area = aor(width, height)
            print(f'The area is {area:.6f}')
        elif shape == 'circle':
            radius = int(input('Give the radius: '))
            area = aoc(radius)
            print(f'The area is {area:.6f}')
        else:
            print('Unknown shape!')

if __name__ == "__main__":
    main()
