import random

# SPOSÓB 1
def Scal(T, lewy, srodek, prawy):
    i = lewy
    j = srodek + 1
    k = lewy

    Pom = [0] * len(T)
    while i <= srodek and j <= prawy:
        if T[i] < T[j]:
            Pom[k] = T[i]
            i += 1
        else:
            Pom[k] = T[j]
            j += 1
        k += 1

    while i <= srodek:
        Pom[k] = T[i]
        i += 1
        k += 1

    while j <= prawy:
        Pom[k] = T[j]
        j += 1
        k += 1

    for i in range(lewy, prawy + 1):
        T[i] = Pom[i]

def Sortuj(T, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy + prawy) // 2
        Sortuj(T, lewy, srodek)
        Sortuj(T, srodek + 1, prawy)
        Scal(T, lewy, srodek, prawy)

# SPOSÓB 2
def Scal_1(T1, T2):
    wynik = []
    i = 0
    j = 0
    n1 = len(T1)
    n2 = len(T2)
    while i < n1 and j < n2:
        if T1[i] < T2[j]:
            wynik.append(T1[i])
            i += 1
        else:
            wynik.append(T2[j])
            j += 1
    wynik.extend(T1[i:])
    wynik.extend(T2[j:])
    return wynik

def SortowaniePrzezScalanie(T):
    n = len(T)
    if n > 1:
        srodek = (n - 1) // 2
        lewy = SortowaniePrzezScalanie(T[:srodek + 1])
        prawy = SortowaniePrzezScalanie(T[srodek + 1:])
        return Scal_1(lewy,prawy)
    return T

    # pass --> instrukcja pusta

# Zad 1
def Zad_1():
    T = list(map(int, input("Podaj ciąg: ").split(" ")))

    Sortuj(T, 0, len(T) - 1)
    print(T)

def Zad():
    T = list(map(int, input("Podaj ciąg: ").split(" ")))

    print(T)
    print(SortowaniePrzezScalanie(T))


# Zad 2
def Zad_2():
    plik = open("ciagi.txt", "r")
    Ciag_1 = list(map(int, plik.readline().split()))
    Ciag_2 = list(map(int, plik.readline().split()))

    print(Ciag_1)
    print(Ciag_2)
    plik.close()

    plik = open("wyniki_2.txt", "w")
    wynik = Scal_1(Ciag_1, Ciag_2)
    plik.write(" ".join(map(str, wynik)))
    plik.close()

# Zad 3
def Zad_3():
    Liczby = [random.randint(1, 1000000) for i in range(1000000)]
    Liczby = SortowaniePrzezScalanie(Liczby)

    with open("wyniki_3.txt", "w") as plik:
        for e in Liczby:
            plik.write(f"{e}\n")
