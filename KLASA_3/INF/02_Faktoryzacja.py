def algorytmFaktoryzacjaLista():
    n = int(input("Podaj: "))
    czynnik = 2
    DzielnikiPierwsze = []

    while n > 1:
        while n % czynnik == 0:
            DzielnikiPierwsze.append(czynnik)
            n = n // czynnik
        czynnik += 1

    return DzielnikiPierwsze

def Zad_1():
    n = int(input("Podaj: "))
    czynnik = 2

    while n > 1:
        while n % czynnik == 0:
            print(czynnik)
            n = n // czynnik
        czynnik += 1

def Zad_2():
    n = int(input("Podaj: "))
    czynnik = 2
    suma = 0

    while n > 1:
        while n % czynnik == 0:
            suma += czynnik
            n = n // czynnik
        czynnik += 1

    return suma

def czyPierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def Zad_3():
    suma = Zad_2()
    print(suma)

    if czyPierwsza(suma):
        print("Suma czynników pierwszych jest pierwsza")
    else:
        print("Suma czynników pierwszych nie jest pierwsza")

def Zad_4():
    DzielnikiPierwsze = algorytmFaktoryzacjaLista()
    Dzielniki = []

    for i in DzielnikiPierwsze:
        if i not in Dzielniki:
            Dzielniki.append(i)

    print(len(Dzielniki))

def Zad_5():
    n = int(input("Czy liczba Smitha: "))
    dzielnik = n
    czynnik = 2
    sumaCzynnikow = 0

    while dzielnik > 1:
        while dzielnik % czynnik == 0:
            dzielnik //= czynnik
            sumaCzynnikow += SumaCyfr(czynnik)
        czynnik += 1

    print(SumaCyfr(n), " ", sumaCzynnikow)
    if SumaCyfr(n) == sumaCzynnikow and czyZlozona(n):
        print("Tak")
    else:
        print("Nie")

def SumaCyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba //= 10
    return suma

def czyZlozona(n):
    if n < 2:
        return False
    pierwiastek = int(math.sqrt(n))
    for i in range(2, pierwiastek + 1):
        if n % i == 0:
            return True
    return False
