#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, value: str):
        self.start = value
    
    def write(self, message:str):
        print(f"{self.start}{message}")

def main():
    pass

if __name__ == "__main__":
    main()
