import random


def Zad_1():
    L = [random.randint(1, 1000) for i in range(100)]
    min = L[0]
    maks = L[0]

    for i in range(len(L)):
        if (L[i] < min):
            min = L[i]
        if (L[i] > maks):
            maks = L[i]

    print(min, maks)

### Zadanie 2 ###
#   Liczba powtórzeń:
#       1 + ((n - 2)/2) * 3 = 1 + (3/2) * (n - 2) = 1 + (3/2)n - 3 = (3/2)n - 2
#
#   n = 10
#   i = 2, 4, 6, 8
#   n = 12

def Zad_3():
    T = [random.randint(1, 1000) for i in range(100)]
    n = len(T)
    minT = maxT = 0
    if T[0] < T[1]:
        min = T[0]
        maxT = T[1]
    else:
        minT = T[1]
        maxT = T[0]

    for i in range(2, n - 2, 2):
        if (T[i] < T[i + 1]):
            if (T[i]) < minT:
                minT = T[i]
            if (T[i + 1] > maxT):
                maxT = T[i + 1]
        else:
            if (T[i + 1]) < minT:
                minT = T[i + 1]
            if (T[i] > maxT):
                maxT = T[i]

    print(minT, maxT)
