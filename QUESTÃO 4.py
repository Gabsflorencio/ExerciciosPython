from cmath import *
import numpy as np 
import math

def aprox_cosh(x,n):
    cosh_aprox = 0
    for k in range(n):
        num = x**(2*k)
        sob = math.factorial(2*k)
        cosh_aprox += (num/sob)
    
    return cosh_aprox
    
x = np.array([1,2,3])
n = 10
valor = aprox_cosh(x,n)

print(f'Os valores são respectivamente:{valor};')