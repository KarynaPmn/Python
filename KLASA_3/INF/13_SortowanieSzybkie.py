def SzybkieSortowanieReku(ciag, lewy, prawy):
    i = lewy
    j = prawy
    pivot = ciag[(i + j) // 2]
    while i <= j:
        while ciag[i] < pivot:
            i += 1
        while ciag[j] > pivot:
            j -= 1
        if i <= j:
            pom = ciag[i]
            ciag[i] = ciag[j]
            ciag[j] = pom
            i += 1
            j -= 1
    if j > lewy:
        SzybkieSortowanieReku(ciag, lewy, j)
    if i < prawy:
        SzybkieSortowanieReku(ciag, i, prawy)

def Zad_1():
    plik = open("liczby.txt", "r")

    Ciag = list(map(int, plik.readlines()))
    SzybkieSortowanieReku(Ciag, 0, len(Ciag) - 1)
    print(Ciag)

    plik.close()

def SzybkieSortowanie(ciag):
    n = len(ciag)
    if (n < 2):
        return ciag
    pivot = ciag[n // 2]
    lewy = [x for x in ciag if x < pivot]
    srodek = [x for x in ciag if x == pivot]
    prawy = [x for x in ciag if x > pivot]

    return SzybkieSortowanie(lewy) + srodek + SzybkieSortowanie(prawy)

def Zad_2():
    plik = open("liczby.txt", "r")

    Ciag = list(map(int, plik.readlines()))
    C = SzybkieSortowanie(Ciag)
    print(C)

    plik.close()

def SzybkieSortowanie_Zad_3(ciag):
    n = len(ciag)
    if (n < 2):
        return ciag
    pivot = ciag[n // 2]

    # for x in ciag:
    #     x < pivot:
    #         lewy =
    #     x == pivot:
    #         srodek =
    #     x > pivot;
    #         prawy =

    return SzybkieSortowanie(lewy) + srodek + SzybkieSortowanie(prawy)

def Zad_3():

Zad_2()
