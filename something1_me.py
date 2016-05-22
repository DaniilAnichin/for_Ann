#!/usr/bin/python
# -*- coding: utf-8 -*-


def int_input(read_string):
    while True:
        try:
            res_numb = int(raw_input(read_string))
        except ValueError:
            print 'Error: Unsupported type, not a number'
        else:
            return res_numb


def main():
    x = int_input("Input any number: ")
    if 1 <= x < 4:
        s = raw_input("Enter a string: ")
        n = int_input("Enter  the number of repetitions of string: ")
        print s*n
    elif 4 <= x < 7:
        m = int_input("Enter a exponent: ")
        print x**m
    elif 7 <= x < 10:
        n = 0
        while n < 10:
            print(x)
            n += 1
            x += 1
    else:
        print("Error")


if __name__ == "__main__":
    main()