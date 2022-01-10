import numpy as np 
import math

def func_x(x,n):
    umporX=0
    for k in range(n):
        if umporX<(1/x):
            umporX+=((-1)**k)*((x-1)**k)
    return umporX

def func_sen(x,n):
    y = 0
    
    for k in range(n):
        y = y+(((-1)**k * (x)**(2*k+1)) / np.math.factorial(2*k+1));
    
    return y    
    
x=0.001
n=5
n1=1
Va=0
tol = 10**-5
erro=1

while (erro>tol):
    Va=func_sen(x,n)*func_x(x,n1)
    erro=(abs(1-Va))
    n1+=1
    
print(f'o erro absoluto foi:{erro}.')
print(f'o valor aproximado fica:{Va}.')