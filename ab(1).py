#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

print "a * x**2 + b * x + c = 0"
a = int(raw_input("Input a: "))
b = int(raw_input("Input b: "))
c = int(raw_input("Input c: "))
d = b**2 - 4 * a * c
e = -b / (a * 2)
f = abs(d)/(a * 2)

if d < 0:
    g = complex(e, f)
    h = g.conjugate()
else:
    g = e + f
    h = e - f
print "x(1) and x(2) are ", g, "and ", h	

