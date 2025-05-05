
"""
Created on Sat Jan 25 16:52:04 2025

@author: VITTHAL PATIL
"""

"program for birge vieta method"

import numpy as np

n=int(input("enter the degree of equations \t"))

A=np.array([0.0 for i in range(n+1)])
B=np.array([0.0 for i in range(n+1)])
C=np.array([0.0 for i in range(n)])

p0=float(input("enter the initial aproximation of root\t"))

iter=int(input("enter the no. of iterations\t"))

for i in range(n+1):
    print("enter coefficient of x%d"%(n-i))
    A[i]=float(input())
    
i=0

while(i<iter):
   print("applying %d iteration of BVM\n"%(i+1))
   print("BVM table is \n")
   print(A)
   B[0]=A[0]
   C[0]=B[0]
   j=1
   while(j<(n+1)):
       B[j]=A[j]+p0*B[j-1]
       j=j+1
      
       
   j=1
   while(j<(n)):
       C[j]=B[j]+p0*C[j-1]
       j=j+1
            
   
   print(B)
   print(C)
   
   p1=p0-(B[n]/C[n-1])
   
   print("the next approximation of root is",)
   
   i=i+1
   p0=p1
   
print("program ended")    
    
    
    
OUTPUT


enter the degree of equations 	3
enter the initial aproximation of root	0.5
enter the no. of iterations	2
enter coefficient of x3
1
enter coefficient of x2
-1
enter coefficient of x1
-1
enter coefficient of x0
1
applying 1 iteration of BVM

BVM table is 

[ 1. -1. -1.  1.]
[ 1.    -0.5   -1.25   0.375]
[ 1.    0.   -1.25]
the next approximation of root is
applying 2 iteration of BVM

BVM table is 

[ 1. -1. -1.  1.]
[ 1.    -0.2   -1.16   0.072]
[ 1.    0.6  -0.68]
the next approximation of root is
program ended
