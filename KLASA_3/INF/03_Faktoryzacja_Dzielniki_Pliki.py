import math

#ciag = plik.read() # wczyta wszystkie linie do tablicy
#ciag = plik.readline() # wczyta telko jedną linię do tablicy
#ciag = plik.readlines() # wczyta wszystkie linie oraz wiersze do tablicy do tablicy

plik = open("liczby1.txt", "r")
liczby_1 = list(map(int, plik.read().split()))
plik.close()

plik = open("liczby2.txt", "r")
liczby_2 = list(map(int, plik.read().split()))
plik.close()

def CzyPierwsza(n):
    if n < 2:
        return False
    pierwiastek = int(math.sqrt(n))
    for i in range(2, pierwiastek + 1):
        if n % i == 0:
            return False
    return True

def Zad_1():
    ile = 0
    for liczba in liczby:
        if CzyPierwsza(liczba):
            ile += 1
    print(ile)

def liczbaDzielnikowWlasciwych(n):
    ile = 0
    for i in range(1, n):
        if n % i == 0:
            ile += 1
    return ile

def Zad_3():
    suma = 0
    for liczba in liczby_2:
        suma += liczbaDzielnikowWlasciwych(liczba)
    print(suma)

def sumaCzynnikowPierwszych(n):
    czynnik = 2
    suma = 0
    while n > 1:
        while n % czynnik == 0:
            suma += czynnik
            n //= czynnik
        czynnik += 1
    return suma

def Zad_5():
    sumaCzynnikow = []
    for liczba in liczby_2:
        sumaCzynnikow.append(sumaCzynnikowPierwszych(liczba))
    minimum = min(sumaCzynnikow)
    for i in range(len(liczby_2)):
        if sumaCzynnikow[i] == minimum:
            print(liczby_2[i])
