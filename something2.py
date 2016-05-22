#!/usr/bin/python
# -*- coding: utf-8 -*-
from something1_me import int_input


def main():
    print "Society at the beginning of the XXI century"
    x = int_input("Enter your age: ")

    if 0<x<8:
        print "You should go to kindergarten"
    elif 7<x<18:
        print "You should go to school"
    elif 17<x<25:
        print "You should go to professional educational establishment"
    elif 24<x<60:
        print "You should go to work"
    elif 59<x<120:
        print "You are a pensioner. You can do everything!"
    else:
        n = 0
        while n < 5:
            print "Error! Try again! " * n
            n +=1

if __name__ == "__main__":
    main()