#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    print "a * x**2 + b * x + c = 0"
    a = int(raw_input("Input a: "))
    b = int(raw_input("Input b: "))
    c = int(raw_input("Input c: "))

    if a == 0:
        x = -c / b
        print "The only solution is %d" % (x)
        return 0
    d = b**2 - 4 * a * c
    e = -b / (a * 2)
    f = abs(d)**0.5 / (a * 2)

    if d < 0:
        print "x(1) and x(2) are {0}+i*{1} and {0}-i*{1}".format(e, f)
    else:
        print "x(1) and x(2) are ", e + f, "and ", e - f

	
if __name__ == '__main__':
    main()