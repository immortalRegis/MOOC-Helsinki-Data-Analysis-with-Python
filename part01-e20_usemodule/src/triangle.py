# Enter you module contents here
"""This module has two functions that calculate the length
 of the hypotenuse and area of right angle triangle given 2 sides"""
__author__ = 'shegs'
__version__ = '1.0.1'

from math import sqrt
def hypothenuse(a, b):
    """This function returns the length of the hypotenuse of a 
    right-angled triangle given the lengths of the 2 other sides"""
    return sqrt(a*a + b*b)

def area(a, b):
    """
    This function calculates the area of a right-angled triangle
    given the lengths of 2 perpendicular sides.
        
    """
    return 0.5 * a * b