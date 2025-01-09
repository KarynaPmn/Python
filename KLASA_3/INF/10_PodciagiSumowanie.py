plik = open("ciagi.txt", "r")
Ciag = list(map(int, plik.read().split()))

# Zad 1
def Zad_1(Ciag):
    maksSuma = 0
    suma = 0

    for i in range(len(Ciag) - 2):
        suma = Ciag[i] + Ciag[i + 1] + Ciag[i + 2]
        print(suma)
        if maksSuma < suma:
            maksSuma = suma

    print(maksSuma)

Zad_1(Ciag)
