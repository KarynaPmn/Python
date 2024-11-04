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

def Scal2(T):
    if len(T) > 1:
        mid = len(T) // 2
        L = T[:mid]
        R = T[mid:]
        
        Scal2(L)
        Scal2(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            T[k] = R[j]
            j += 1
            k += 1

# Zad 1
def Zad_1():
    T = list(map(int, input("Podaj ciąg: ").split(" ")))

    Sortuj(T, 0, len(T) - 1)
    print(T)

Zad_1()
