import numpy as np 
import math

def func_x(x):
    funX=x**2
    
    return funX

def exp_dupla(x,n):
    exp_aprox = 0
    for k in range(n):
        num = (func_x(x))**k
        sob = math.factorial(k)
        exp_aprox += num/sob
        
    return exp_aprox
    
x = np.array ([1,2,3])
n = 21
out = exp_dupla(x,n)

print(out)