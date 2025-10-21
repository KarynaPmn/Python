import random

def Zad_3():
    M = [
        [3, 7, 2, 6, 4],
        [5, 1, 9, 3, 8],
        [6, 2, 4, 7, 1],
        [8, 3, 5, 2, 9],
        [4, 6, 1, 5, 7]
    ]

    for t in M:
        print(t)

    n = len(M)
    i = 0
    j = 0
    suma = M[0][0]
    M[0][0] = "X"
    while(i < n - 1 or j < n - 1):
        if (i == n - 1):
            j += 1
        elif (j == n - 1):
            i += 1
        elif (int(M[i + 1][j])> int(M[i][j + 1])):
            i += 1
        else:
            j += 1
        suma += int(M[i][j])
        M[i][j] = "X"

    print()
    for t in M:
        print(t)
    print(suma)

def Zad_4():
    plik = open("macierz.txt", "r")
    M = []
    for line in plik:
        M.append(list(map(int, line.split())))
    plik.close()

    I = [[0, 0]]
    n = len(M)
    i = 0
    j = 0
    suma = M[0][0]
    while (i < n - 1 or j < n - 1):
        if (i == n - 1):
            j += 1
        elif (j == n - 1):
            i += 1
        elif (int(M[i + 1][j]) > int(M[i][j + 1])):
            i += 1
        else:
            j += 1
        I.append([i, j])
        suma += int(M[i][j])

    print(suma)
    for i in I:
        print(i[0], " ", i[1])

def Zad_5():
    n = int(input("Podaj n: "))
    M = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

    for t in M:
        for e in t:
            print(e, end="\t")
        print()

    i = 0
    j = 0
    suma = M[0][0]
    while i < n - 1 or j < n - 1:
        if i == n - 1:
            j += 1
        elif j == n - 1:
            i += 1
        elif M[i + 1][j] > M[i][j + 1]:
            i += 1
        else:
            j += 1
        
        suma += M[i][i]

    print("Największa suma: ", suma)
