Nikhil Pawar
SEL28
Date-03-02-2025

"Program For Gauss Jacobi Method"

def fx(x,y,z):
    return(1/6*(28+6*y+11*z))

def fy(x,y,z):
    return(1/4*(7-3*x))

def fz(x,y,z):
    return(-1/5*(2+3*x-11*y))

n=int(input("Enter No. of Iterations \t"))
x0=float(input("Enter the initial value of x \t"))
y0=float(input("Enter the initial value of y \t"))
z0=float(input("Enter the initial value of z \t"))

for i in range (n):
    print("Applying %d iteration of Gauss Jacobi Method"%(i+1))
    x1=fx(x0,y0,z0)
    y1=fy(x0,y0,z0)
    z1=fz(x0,y0,z0)
    print("The approx solution value is (%f, %f, %f)"%(x1,y1,z1))
    x0=x1
    y0=y1
    z0=z1
    
print("The iteration ended\n") 

OUTPUT :-

Enter No. of Iterations 	5
Enter the initial value of x 	0
Enter the initial value of y 	0
Enter the initial value of z 	0
Applying 1 iteration of Gauss Jacobi Method
The approx solution value is (4.666667, 1.750000, -0.400000)
Applying 2 iteration of Gauss Jacobi Method
The approx solution value is (5.683333, -1.750000, 0.650000)
Applying 3 iteration of Gauss Jacobi Method
The approx solution value is (4.108333, -2.512500, -7.660000)
Applying 4 iteration of Gauss Jacobi Method
The approx solution value is (-11.889167, -1.331250, -8.392500)
Applying 5 iteration of Gauss Jacobi Method
The approx solution value is (-12.050833, 10.666875, 3.804750)
The iteration ended
