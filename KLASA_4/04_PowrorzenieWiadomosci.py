
from itertools import count
def Zad_1():
    plik = open("dane.txt", "r")
    Nominaly = list(map(int, plik.readline().split()))
    Kwoty = list(map(int, plik.readlines()))
    minIloscNominalul = float("Inf")
    minIlN = []
    minList = []

    for kwota in Kwoty:
        N = []
        ileNominalow = 0
        temp = kwota
        for nominal in Nominaly:
            ileM = 0
            while (temp - nominal > 0):
                ileM += 1
                ileNominalow += 1
                N.append(nominal)
                temp -= nominal

        if (ileNominalow < minIloscNominalul):
            minIloscNominalul = ileNominalow
            minList.append(kwota)
            minIlN.append(ileNominalow)

    # Nie zakończone!
    # if (minIlN.count(minIlN[-1])):
        # for _ in range(len())

    print(minList[-1])

Zad_1()
