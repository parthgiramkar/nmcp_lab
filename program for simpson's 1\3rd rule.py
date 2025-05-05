Created on Mon Feb 17 13:57:50 2025

@author: VITTHAL
"""
"program for simpson's 1/3rd rule"

import numpy as np
def f(x):
    return(1/(1+x))


a=float(input("Enter lower limit\t"))
b=float(input("Enter upper limit\t"))

n=int(input("enter sub intervals\t"))
        
h=(b-a)/(1.0*n)

sum=0

x=np.array([0.0 for i in range(n+1)])

x[0]=a
i=1
while i<n+1:
    x[i]=x[i-1]+h
    i=i+1
    
for i in range(n+1):
    if(i==0):
        sum=sum+f(a)
    elif(i==n):
        sum=sum+f(b)
    elif(i%2!=0):
        sum=sum+4*(f(x[i]))
    else:
        sum=sum+2*(f(x[i]))
        
intg=h/3*sum

print("The value of numerical integration is",intg)        
            
OUTPUT

runfile('C:/Users/PLC LAB-13/vitthal.py', wdir='C:/Users/PLC LAB-13')
Enter lower limit	0
Enter upper limit	6
enter sub intervals	10
The value of numerical integration is 1.9485191477540889
