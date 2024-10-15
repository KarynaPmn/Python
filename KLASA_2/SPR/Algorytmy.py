# METODY NUMERYCZNE 

def f(x):
    return x**3 - 2*x - 5

# prostokąt

def ProstokatP(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + dx * i) * dx
    return suma

def ProstokatS(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + dx * i + dx / 2) * dx
    return suma

def ProstokatK(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + dx * i + dx) * dx
    return suma

# trapez 

def Trapez(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += ((f(a + dx * i) + f(a + dx * i + dx)) * dx) / 2
    return suma

# trójkąt
def Trojkat(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += (f(a + dx * i + dx) * dx) / 2
    return suma

# romb
def Romb(a, b, n):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += (f(a + dx * i + dx / 2) * dx) / 2
    return suma

#  BISEKCJA

def Bisekcja(a, b, d):
    krok = 0
    while abs(a - b) > d:
        x = (a + b) / 2

        if (a == b):
            break
        elif(f(x) <= 0):
            a = x
        elif(f(x) > 0):
            b = x

        krok += 1
        print("Krok", krok, "--- A:", a, "i B:", b)
    return krok

def znowuBis(a, b, eps):
    def f1(x):
        return x**3 - x - 2
    
    
    while abs(a - b) > eps:
        x = (a + b) / 2
        if f1(a) * f1(x) <= 0:
            b = x
        else:
            a = x
        print(x)

#print(Bisekcja(0, 2, 0.01))

# LEADER

T = [2, 1, 1, 3, 1, 2, 1, 2]

def Leader(T):
    leader = T[0]
    ilosc = 0

    for i in range(len(T)):
        if ilosc == 0:
            leader = T[i]
            ilosc = 1
        else:
            if leader == T[i]:
                ilosc += 1
            else:
                ilosc -= 1
    
    ile_l = 0
    for i in range(len(T)):
        if T[i] == leader:
            ile_l += 1
    if ile_l > len(T) // 2:
        print(leader)
    else:
        print("Ni ma lideara.")

# Leader(T)


#METODA NEWTONA-RAPHSON

def PierwiastekNewtonRaphson(p, epsilon):
    a = p
    b = p / a

    while abs(a - b) > epsilon:
        a = (a + b) / 2
        b = p / a
    
    return a

# print(PierwiastekNewtonRaphson(47, 0.01))

# MONTE-CARLO --> 4*k/p 

from random import uniform
from math import sqrt

def MonteCarlo(ilosc_wylosowan):
    ilosc_wulosowan_trafionych = 0
    for _ in range(ilosc_wylosowan):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if sqrt(x**2 + y**2) <= 1:
            ilosc_wulosowan_trafionych += 1 
    return 4 * ilosc_wulosowan_trafionych / ilosc_wylosowan

# print(MonteCarlo(10000))
