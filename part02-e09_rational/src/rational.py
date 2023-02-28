#!/usr/bin/env python3

from fractions import Fraction
class Rational():
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
    
    def __add__(self, another:"Rational"):
        denominator = max(self.n2, another.n2)
        while not ((denominator % self.n2 == 0) and (denominator % another.n2 == 0)):
            denominator += 1 

       
        numerator = (denominator//self.n2)*(self.n1) + (denominator//another.n2)*(another.n1) 
        return Rational(numerator, denominator)
    
    def __sub__(self, another:"Rational"):
        denominator = max(self.n2, another.n2)
        while not ((denominator % self.n2 == 0) and (denominator % another.n2 == 0)):
            denominator += 1 

        numerator = (denominator//self.n2)*(self.n1) - (denominator//another.n2)*(another.n1) 
        return Rational(numerator, denominator)
    
    def __mul__(self, another:"Rational"):
        denominator = self.n2 * another.n2
        numerator = (self.n1) * (another.n1) 
        return Rational(numerator, denominator)
    
    def __truediv__(self, another:"Rational"):
        denominator = self.n2 * another.n1
        numerator = (self.n1) * (another.n2) 
        return Rational(numerator, denominator)
    
    def __gt__(self, another:"Rational"):
        value = Fraction(self.n1, self.n2) > Fraction(another.n1, another.n2)
        return value
    
    def __lt__(self, another:"Rational"):
        value = Fraction(self.n1, self.n2) < Fraction(another.n1, another.n2)
        return value

    def __eq__(self, another:"Rational"):
        value = Fraction(self.n1, self.n2) == Fraction(another.n1, another.n2)
        return value
        
    def __str__(self):
        return (f'{self.n1}/{self.n2}')


def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
