#Inggrit Pondaag
#19021106027

import numpy as np

def func(x) :
    return x**3 + (2*x)**2 + (10.0*x) - 20.0

xi = 1.0
xf = 1.5
tol = 0.0000001

if func(xi) * func(xf) > 0:
    print('tidak punya akar fungsi')
xb = xf- (func(xf) * (xf-xi)) / (func(xf) - func(xi))
while abs(func(xb)) > tol :
    xb = xf- (func(xf) * (xf-xi)) / (func(xf) - func(xi))
    if func(xi) * func(xb) > 0 :
        xi = xb
        print ('akar adalah = ',xi)
        break
    if func(xf) * func(xb) > 0 :
        xf = xb
        print('akar adalah = ',xf)
        break
