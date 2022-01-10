from cmath import *
import numpy as np 
import math

def fun_cos(x,n):
    cos_aprox = 0
    for k in range(n):
        coef = (-1)**k
        num = x**(2*k)
        den = math.factorial(2*k)
        cos_aprox += (coef)*(num/den)
    return cos_aprox
    
def func_sen(x,n,j):
    y = 0
    
    for k in range(n):
        y = y + (((-1)**k * (x)**(2*k+1)) / np.math.factorial(2*k+1))*j;
        
    return y
    


float (tau)
j=complex(0,1)
x=45
x_rad = (math.radians(x))
n=0
tol=10**-6
while (tau>tol):
    out1=(func_sen(x_rad,n,j) + fun_cos(x_rad,n))
    tau=(abs(out - out1))
    n+=1
print(f'O erro fica:{tau};')
print(f'O valor aproximado:{out1};')