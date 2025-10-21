from math import ceil
import sys


def AlgorytmZachlanny(Nominaly, kwota):
    iloscNominalow = 0

    for nominal in Nominaly:
        ile = kwota // nominal
        iloscNominalow += ile
        kwota %= nominal

    return iloscNominalow


def Zad_1():
    plik = open("dane.txt", "r")
    Nominaly = list(map(int, plik.readline().split()))
    Kwoty = list(map(int, plik.readlines()))
    minIloscNominslow = sys.maxsize

    plik.close()

    for kwota in Kwoty:
        iloscNominalow = AlgorytmZachlanny(Nominaly, kwota)

        if iloscNominalow < minIloscNominslow:
            minIloscNominslow = iloscNominalow
    
    print("Najmniejszą ilość nominałów (", minIloscNominslow ,") ma: ", end="")
    for kwota in Kwoty:
        if AlgorytmZachlanny(Nominaly, kwota) == minIloscNominslow:
            print(kwota, end=" ")
    print()

def Zad_2():
    M = []
    suma = 0
    kierunek = ""
    with open("macierz.txt", "r") as plik:
        M = [list(map(int, linia.split())) for linia in plik]
    
    

    n = len(M)
    i = 0
    j = 0
    while i < n - 1 or j < n - 1:
        if i == n - 1:
            j += 1
            kierunek += "P"
        elif j == n - 1:
            i += 1
            kierunek += "D"
        elif M[i][j + 1] > M[i + 1][j]:
            j += 1
            kierunek += "P"
        else:
            i += 1
            kierunek += "D"

        suma += M[i][j]

    for t in M:
        for e in t:
            print(e, end="\t")
        print()
        
    print(kierunek)
    print(suma)
        

Zad_2()
