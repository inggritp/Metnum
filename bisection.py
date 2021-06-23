#Inggrit Pondaag
#19021106027

import numpy as np

def func(x) :
    return x**3 + (2*x)**2 + (10.0*x) - 20.0

xi = 1.0
xf = 1.5
tol = 0.0000001
maxiter = 200
if func(xi) * func(xf) > 0:
    print('tidak punya akar fungsi')
else :
    for i in range(maxiter):
        xb = 0.5 *(xi + xf)
        if func(xi) * func(xb) < 0:
            xf = xb
        else :
            xi = xb
        if abs(xi-xf) < tol :
            akar = xb
            print ('akar = ',akar)
            break
