#!\usr\bin\python
# -*- coding: utf-8 -*-

a = int(raw_input ("Input a:"))
b = int(raw_input ("Input b:"))
c = int(raw_input ("Input c:"))

if a < b + c and a > abs(b - c) and b < a + c and b > abs(a - c) and c < a + b and c > abs(a - b):
    square = ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 / 4
    if c**2 > a**2 + b**2 or a**2 > c**2 + b**2 or a**2 > c**2 + b**2:
	    print "It is amblygon. Square is ", square
    elif c**2 == a**2 + b**2 or a**2 == c**2 + b**2 or b**2 == a**2 + c**2:
        print "It is rectangular triangle. Square is ", square
    elif c**2 < a**2 + b**2 or a**2 < c**2 + b**2 or b**2 < a**2 + c**2:
        print "It is oxygon. Square is ", square
else:
    print "It is not a triangle"