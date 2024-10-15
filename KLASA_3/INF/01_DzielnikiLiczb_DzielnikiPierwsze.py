def czy_podzielna_przez_2(n):
    return n % 2 == 0

n = int(input("Podaj: "))
if czy_podzielna_przez_2(n):
    print("Tak")
else:
    print("Nie")

def dzielniki_1(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()

def dzielniki_2(n): # pierwiasten(n) - 1
    i = 1
    while i * i < n:
        if n % i == 0:
            print(int(i), end=" ")
            print(int(n / i), end=" ")
        i = i + 1
    if i * i == n:
        print(int(i), end=" ")
    print()
dzielniki_2(n)

def suma_dzielnikow(n):
    suma = 0
    for i in range(1, n + 1):
        if n % i == 0:
            suma += i
    print(suma)
suma_dzielnikow(n)

# Zad 5
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Podaj liczbę: "))
for i in range(2, n + 1):
    if n % i == 0 and czy_pierwsza(i):
            print(i, end=" ")# Zad 5
def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Podaj liczbę: "))
for i in range(2, n + 1):
    if n % i == 0 and czy_pierwsza(i):
            print(i, end=" ")

# Zad 6
a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

if czy_pierwsza(a) and czy_pierwsza(b) and (a - b == 2 or b - a == 2):
    print("Bliźniacze")
else:
    print("Nie")
    
# Zad 7
def czy_doskonala(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        print("Tak")
    else:
        print("Nie")

n = int(input("Podaj liczbę: "))
czy_doskonala(n)

# Zad.8
p = int(input("Podaj liczbę: "))
d = int(input("Podaj liczbę: "))
def sumaDzielnikow(n):
     x = 0
     y = 0
     while (n - 1 != x):
         x = x + 1
         if (n % x == 0):
             y = y + x
     return y
if (sumaDzielnikow(p) == d and sumaDzielnikow(d) == p):
     print("Tak")
else:
     print("Nie")

# Zad.9
def czyLiczbyBlizniacze(p,d):
    def czyDzielnikPierwszy(n):
        x = 0
        y = -1
        while (n != x):
            x = x + 1
            if (n % x == 0):
              y = y + 1
        if (y == 1):
            return True
        else:
            return False
    if (czyDzielnikPierwszy(p) == True and czyDzielnikPierwszy(d) == True):
        if (p - d == 2 or p - d == 2):
            print(p and d)
