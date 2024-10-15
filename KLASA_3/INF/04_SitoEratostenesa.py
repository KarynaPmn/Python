# Zad 1
def SitoEratostenesa(n):
    czyPierwszaList = [True] * (n + 1)
    czyPierwszaList[0] = False
    czyPierwszaList[1] = False

    p = 2
    while p * p <= n:
        if czyPierwszaList[p]:
            for i in range(p * p, n + 1, p):
                czyPierwszaList[i] = False
        p = p + 1

    for i in range(2, n + 1):
        if czyPierwszaList[i] == True:
            print(i, end=" ")

# Zad 2
def SumaSitoEratostenesa(n):
    czyPierwszaList = [True] * (n + 1)
    czyPierwszaList[0] = False
    czyPierwszaList[1] = False

    sumaDzielnikow = 0
    p = 2
    while p * p <= n:
        if czyPierwszaList[p]:
            for i in range(p * p, n + 1, p):
                czyPierwszaList[i] = False
        p = p + 1

    for i in range(2, n + 1):
        if czyPierwszaList[i] == True:
            sumaDzielnikow += i

    print(n, sumaDzielnikow)

# Zad 3
def WhileSitoEratostenesa(n):
    czyPierwszaList = [True] * (n + 1)
    czyPierwszaList[0] = False
    czyPierwszaList[1] = False

    p = 2
    while p * p <= n:
        if czyPierwszaList[p]:
            i = p * p
            while i < n + 1:
                czyPierwszaList[i] = False
                i += p
        p = p + 1

    for i in range(2, n + 1):
        if czyPierwszaList[i] == True:
            print(i, end=" ")

# Zad 4
def SitoErastosenesaList(n):
    CzyPierwszaLista = [True] * (n + 1)
    CzyPierwszaLista[0] = False
    CzyPierwszaLista[1] = False

    p = 2
    while p * p <= n:
        if CzyPierwszaLista[p]:
            for i in range(p * p, n + 1, p):
                CzyPierwszaLista[i] = False
        p += 1

    return CzyPierwszaLista

def Zad_4():
    sumaLiczbZpliku = 0
    plik = open("liczby.txt", "r")
    liczbyList = list(map(int, input().split()))
    plik.close()

    PierwszeLista = SitoErastosenesaList(1000)

    for liczba in liczbyList:
        if PierwszeLista[int(liczba)]:
            sumaLiczbZpliku += 1
    print(sumaLiczbZpliku)

# Zad 5
def SitoErastosenesaPrzedzial(a, b):
    CzyPierwszaLista = [True] * (b + 1)
    CzyPierwszaLista[0] = False
    CzyPierwszaLista[1] = False
    p = a
    while p * p <= b:
        if CzyPierwszaLista[p]:
            for i in range(p * p, b + 1, p):
                CzyPierwszaLista[i] = False
        p += 1

    return CzyPierwszaLista

def Zad_5():
    a, b = map(int, input("Podaj przedział: ").split())
    while a < 2 or a > b:
        print("Błąd! Podaj 2 < a < b")
        a, b = map(int, input("Podaj przedział: ").split())

    czyPierwszeList = SitoErastosenesaPrzedzial(a, b)
    ileLiczbPierwszych = 0
    sumaLiczbPierwszych = 0

    for i in range(a, b + 1):
        if czyPierwszeList[i]:
            print(i, end=" ")
            ileLiczbPierwszych += 1
            sumaLiczbPierwszych += i
    print("\nIlość: ", ileLiczbPierwszych)
    print("Suma: ", sumaLiczbPierwszych)

# Zad 6
def IleSitoErastosenesa(n):
    CzyPierwszaLista = [True] * (n + 1)
    CzyPierwszaLista[0] = False
    CzyPierwszaLista[1] = False

    p = 2
    while p * p <= n:
        if CzyPierwszaLista[p]:
            for i in range(p * p, n + 1, p):
                CzyPierwszaLista[i] = False
        p += 1

    ileLiczb = 0
    for i in range(2, n + 1):
        if CzyPierwszaLista[i]:
            ileLiczb += 1

    return ileLiczb

def Zad_5():
    with open("ciag.txt") as plik:
        ciagList = list(map(int, plik.read().split()))
        ileLiczbPierwszych = IleSitoErastosenesa(1000)
        print(len(ciagList))
        jakiProcentstanowiaPierwsze = round(ileLiczbPierwszych / len(ciagList), 3) * 100

        print("Ile: ", ileLiczbPierwszych)
        print("Procent l.p: ", jakiProcentstanowiaPierwsze)
        plik.close()
