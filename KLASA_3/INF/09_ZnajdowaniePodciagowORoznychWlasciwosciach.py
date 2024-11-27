plik = open("liczby.txt", "r")
Ciag = list(map(int, plik.read().split()))

# Zad 1
def WyswietlLiczbyPoSpacji(Tab):
    print(' '.join(map(str, Tab)))

def Podciagi(Ciag):
    n = len(Ciag)

    for dl in range(1, n + 1):
        for indexPocz in range(n - dl + 1):
            WyswietlLiczbyPoSpacji(Ciag[indexPocz : indexPocz + dl])

def Podciagi_1(Ciag):
    n = len(Ciag)

    for dl in range(1, n + 1):
        for indexPocz in range(n - dl + 1):
            indexKon = indexPocz + dl - 1

            for i in range(indexPocz, indexKon + 1):
                print(Ciag[i], end=' ')
            print()

# Zad 2
def Zad_2(Ciag):
    n = len(Ciag)

    for indexPocz in range(n + 1):
        for i in range(indexPocz, n + 1):
            WyswietlLiczbyPoSpacji(Ciag[indexPocz : i])

# Zad 3 !!! nie dokończone
def SumaCyfr(s):
    suma = 0

    for i in range(len(s)):
        a = int(s[i])
        while a > 0:
            suma += a % 10
            a //= 10

    return suma
def Zad_3(Ciag):
    n = len(Ciag)

    for indexPocz in range(n - 4):
        for i in range(indexPocz, indexPocz + 6):
            print(SumaCyfr(Ciag[indexPocz: i]), end=" - ")
            WyswietlLiczbyPoSpacji(Ciag[indexPocz : i])

# Zad 4 
Zad_3(Ciag)
