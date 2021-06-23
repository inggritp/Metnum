
#Inggrit Pondaag
#19021106027


def func(x) :
    return x**3 + (2*x)**2 + (10.0*x) - 20.0

def tur(x) :
    return (3*x)**2 + (4*x) + 10.0

x0 = 1.0
tol = 0.0000001
maxiter = 200

for iter in range(maxiter) :
    xp = x0-func(x0) / tur(x0)
    if abs(func(xp)) < tol :
        akar = xp
        print('akar = ',akar)
        print('konvergen pada iterasi ke = ', iter)
        break
    else :
        x0 = xp