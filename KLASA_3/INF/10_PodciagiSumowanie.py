plik = open("ciag.txt", "r")
Ciag = list(map(int, plik.read().split()))

def Zad_1(Ciag):
    maksSuma = 0
    suma = 0

    for i in range(len(Ciag) - 2):
        suma = Ciag[i] + Ciag[i + 1] + Ciag[i + 2]

        if maksSuma < suma:
            maksSuma = suma

    print(maksSuma)

def Zad_2(Ciag):
    maksSuma = 0
    suma = 0
    T = []

    for i in range(len(Ciag) - 2):
        suma = Ciag[i] + Ciag[i + 1] + Ciag[i + 2]

        if maksSuma < suma and not maksSuma == suma:
            maksSuma = suma
            T = [Ciag[i], Ciag[i + 1], Ciag[i + 2]]

    print(T)

def Zad_3(Ciag):
    maksSuma = 0
    suma = 0
    T = []
    Temp = []

    for i in range(len(Ciag) - 1):
        Temp = Ciag[i : len(Ciag) - 1]
        suma = sum(Temp)

        if maksSuma < suma:
            maksSuma = suma
            T = Temp

    print(len(T))

def Zad_4(Ciag):
    maksSuma = 0
    aktSuma = 0
    n = len(Ciag)

    for i in range(n):
        aktSuma += Ciag[i]

        if aktSuma < 0:
            aktSuma = 0
        elif aktSuma > maksSuma:
            maksSuma = aktSuma
    
    print(maksSuma)

def Zad_5(Ciag):
    maksSuma = 0
    aktSuma = 0
    aktPocz = 0
    maksKon = 0
    maksPocz = 0
    
    n = len(Ciag)

    for i in range(n):
        aktSuma += Ciag[i]

        if aktSuma < 0:
            aktSuma = 0
            aktPocz = i + 1
        elif aktSuma > maksSuma:
            maksSuma = aktSuma
            maksPocz = aktPocz
            maksKon = i
    
    print(maksSuma, Ciag[maksPocz : maksKon + 1])
