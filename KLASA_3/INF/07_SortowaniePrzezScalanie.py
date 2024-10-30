# Nie zakończone !!!
def Scal(T, lewy, srodek, prawy):
    i = lewy
    j = srodek + 1
    k = lewy

    Pom = []
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

        for i in range(lewy, prawy):
            T[i] = Pom[i]

def Sortuj(T, lewy, prawy):
    if lewy < prawy:
        srodek = (lewy + prawy) // 2
        Sortuj(T, lewy, srodek)
        Sortuj(T, srodek + 1, prawy)
        Scal(T, lewy, srodek, prawy)

# Zad 1
def Zad_1():
    T = list(map(int, input("Podaj ciąg: ").split(" ")))
    Pom = Sortuj(T, 0, len(T) - 1)
    print(Pom)

Zad_1()
