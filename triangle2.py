#!\usr\bin\python
# -*- coding: utf-8 -*-

a = int(raw_input ("Input a:"))
b = int(raw_input ("Input b:"))
c = int(raw_input ("Input c:"))
if a < b + c and a >= b  and a >= c :
    if a**2 > c**2 + b**2 :
        print "It is amblygon. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4
	else :
	    print "It is rectangular triangle. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4
elif b < a + c and b >= a  and b >= c :
    if b**2 > c**2 + a**2 :
        print "It is amblygon. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4
	else :
	    print "It is rectangular triangle. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4	
elif c < a + b and c >= a  and c >= b :
    if c**2 > b**2 + a**2 :
        print "It is amblygon. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4
	else :
	    print "It is rectangular triangle. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4
elif a < b + c and a > b - c and b < a + c and b > a - c and c < a + b and c > a - b :
    print "It is oxygon. Square is ", ((a + b + c) * (a + b - c) * (a + c - b) * (c + b - a )) **0.5 /4		
else :
    print "It is not a triangle"