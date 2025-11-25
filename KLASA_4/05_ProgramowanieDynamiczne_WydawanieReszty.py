### ZADANIE 1 ###

def WydanieReszty(kwota, N):
    max_k = kwota + 1

    LN = [max_k] * (kwota + 1)
    LN[0] = 0

    for i in range(1, kwota + 1):
        for nominal in N:
            if i >= nominal:
                if LN[i - nominal] + 1 < LN[i]:
                    LN[i] = LN[i - nominal] + 1

    return LN[kwota] if LN[kwota] != max_k else -1


def Zad_1():
    with open("nominaly.txt", "r") as plik:
        Nominaly = list(map(int, plik.readline().split()))
    
    print(WydanieReszty(180, Nominaly)) # Wynik: 3


### ZADANIE 2 ###
def WydanieReszty_Nominaly(kwota, N):
    max_k = kwota + 1

    LN = [max_k] * (kwota + 1)
    LN[0] = 0

    T = [-1] * (kwota + 1)  

    for i in range(1, kwota + 1):
        for nominal in N:
            if i >= nominal and LN[i - nominal] + 1 < LN[i]:
                LN[i] = LN[i - nominal] + 1
                T[i] = nominal      

    if LN[kwota] == max_k:
        print(-1)
        return

    W = {}
    i = kwota
    while i > 0:
        nom = T[i]
        W[nom] = W.get(nom, 0) + 1
        i -= nom

    for nom in W:
        print(f"{W[nom]}x{nom}")

    print("Minimalna liczba:", LN[kwota])

                
def Zad_2():
    with open("nominaly.txt", "r") as plik:
        Nominaly = list(map(int, plik.readline().split()))

    WydanieReszty_Nominaly(180, Nominaly)

### ZADANIE 3 ###
def WydanieReszty_Kwota(kwota, N):
    max_k = kwota + 1
    L = [max_k] * (kwota + 1)
    L[0] = 0

    for i in range(1, kwota + 1):
        for nominal in N:
            if i >= nominal:
                if L[i - nominal] + 1 < L[i]:
                    L[i] = L[i - nominal] + 1
    
    return L[kwota] if L[kwota] != max_k else -1

def Zad_3():
    with open("dane.txt") as plik:
        Nominaly = list(map(int, plik.readline().split()))
        Kwoty = list(map(int, plik.readlines()))

    min_k = Kwoty[-1]
    W = {}
    for kwota in Kwoty:
        nom = WydanieReszty_Kwota(kwota, Nominaly)

        if nom <= min_k:
            W[kwota] = nom
            min_k = nom
        
    for nom in W:
        print(nom)
