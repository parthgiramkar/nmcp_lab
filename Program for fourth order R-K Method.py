Name-VITTHAL PATIL
Roll no.-24
Date-03/03/2025


code-

"""

Program for fourth order R-K Method

"""

import math

def f(x,y):
    return (math.sqrt(x+y))

x0=float(input("Enter the initial value of x\t"))
y0=float(input("Enter the initial value of y\t")) 

h=float(input("enter the step size(h)\t"))

x=float(input ("Enter the value of x for which y is  to be clculated\t"))

n=int((x-x0)/h)


for i in range(n):
    print("applying the %d iteration of fourth order R-K method"%(i+1))
    k1=h*f(x0,y0)
    k2=h*f(x0+h/2,y0+k1/2)
    k3=h*f(x0+h/2,y0+k2/2)
    k4=h*f(x0+h,y0+k3)
    
    k=1/6*(k1+2*k2+2*k3+k4)
    
    y1=y0+k
    x1=x0+h
    print ("the value of x=%f is %f"%(x1,y1))
    x0=x1
    y0=y1
    

print("the iteration ended")    

    

output-

Enter the initial value of x	0
Enter the initial value of y	1
enter the step size(h)	0.2
Enter the value of x for which y is  to be clculated	0.2
applying the 1 iteration of fourth order R-K method
the value of x=0.200000 is 1.219403
the iteration ended
