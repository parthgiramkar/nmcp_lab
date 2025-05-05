
"""
Created on Sat Jan 25 16:16:17 2025

@author: VITTHAL PATIL

"""
"program for bisection method"

import math

def f(x):
    return(math.cos(x)-x*math.exp(x))

a=float(input("enter the 1st value of interval\t"))
b=float(input("enter the 1st value of interval\t"))

iter=int(input("enter no. of iterations \t"))

i=0
while(i<iter):
    print("applying %d iteration of bisection method\n"%(i+1))
    m=(a+b)/2
    
    if(f(a)*f(m)<0):
        b=m
    else:
        a=m
        
    print("the new interval is (%f,%f)"%(a,b)) 
    i=i+1
print("the program ended")


OUTPUT


enter the 1st value of interval	0
enter the 1st value of interval	1
enter no. of iterations 	5
applying 1 iteration of bisection method

the new interval is (0.500000,1.000000)
applying 2 iteration of bisection method

the new interval is (0.500000,0.750000)
applying 3 iteration of bisection method

the new interval is (0.500000,0.625000)
applying 4 iteration of bisection method

the new interval is (0.500000,0.562500)
applying 5 iteration of bisection method

the new interval is (0.500000,0.531250)
the program ended
