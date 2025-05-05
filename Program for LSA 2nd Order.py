VITTHAL PATIL 
SEL 24


Code:

"Program for LSA 2nd Order"

import numpy as np
import sympy as sy


n=int(input("Enter the no. of observations\t"))

x=np.array([0 for i in range(n)])
y=np.array([0 for i in range(n)])

for i in range(n):
    print("Enter the value of x%d"%(i))
    x[i]=float(input())
    print("Enter the value of y%d"%(i))
    y[i]=float(input())
    
x2=x*x
x3=x2*x
x4=x3*x
xy=x*y
x2y=x2*y
    
Sx=0
for i in x:
    Sx=Sx+i
        
Sy=0
for i in y:
    Sy=Sy+i  
        
    
Sx2=0
for i in x2:
    Sx2=Sx2+i
        
Sx3=0
for i in x3:
    Sx3=Sx3+i
        
Sx4=0
for i in x4:
    Sx4=Sx4+i
         
Sxy=0
for i in xy:
    Sxy=Sxy+i
         
Sx2y=0 
for i in x2y:
    Sx2y=Sx2y+i
        
        
order=int(input("Enter the Order of LSA(1 or 2)"))
    
a=sy.symbols('a')
b=sy.symbols('b')     
c=sy.symbols('c')
    
    
    
if(order==1):
    print("\nSolving for 1st order LSA\n")
    eq1=sy.Eq(n*a+b*Sx,Sy)
    eq2=sy.Eq(n*a+b*Sx,Sy)
    sol=sy.solve((eq1,eq2),(a,b))
elif(order==2):
    print("\nSolving for 2nt order LSA\n")
    eq1=sy.Eq(n*a+b*Sx+c*Sx2,Sy)
    eq2=sy.Eq(a*Sx+b*Sx2+c*Sx3,Sxy)
    eq3=sy.Eq(a*Sx2+b*Sx3+c*Sx4,Sx2y)
    sol=sy.solve((eq1,eq2,eq3),(a,b,c))
else:
    print("\n Wrong Order Entered\n")
        
print(sol)


Output:

Enter the no. of observations	6
Enter the value of x0
0
Enter the value of y0
0
Enter the value of x1
2
Enter the value of y1
33
Enter the value of x2
4
Enter the value of y2
55
Enter the value of x3
6
Enter the value of y3
70
Enter the value of x4
8
Enter the value of y4
80
Enter the value of x5
10
Enter the value of y5
85
Enter the Order of LSA(1 or 2) 2

Solving for 2nt order LSA

{a: 8/7, b: 2337/140, c: -47/56}
