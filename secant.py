
#Inggrit Pondaag
#19021106027
import numpy as np

def func(x) :
    return x ** 3 + (2 * x) ** 2 + (10.0 * x) - 20.0
x0 = 1.5
x1 = 1.0
tol = 0.0000001
maxiter = 200

for iter in range(maxiter) :
    xp1 = x0 - ((x0-x1) * func(x0) / (func(x0) - func(x1)))
    if abs(func(xp1)) < tol :
        akar = xp1
        print('akar adalah = ',akar)
        print('iterasi ke = ',iter)
        break
    else :
        x1 = x0
        x0 = xp1