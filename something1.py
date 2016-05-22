#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    x = int(raw_input("Input any number "))

    if 0<x<4:
        s = raw_input("Enter a line: ")
        n = int(raw_input("Enter  the number of repetitions of line: "))
        print s*n
    elif 3<x<7:
        m = int(raw_input("Enter a degree: "))
        print x**m
    elif 6<x<10:
        n = 0
        while n<10:			
            print(x)
            n +=1
            x +=1
    else:
        print("Error")

if __name__ == "__main__":
    main()