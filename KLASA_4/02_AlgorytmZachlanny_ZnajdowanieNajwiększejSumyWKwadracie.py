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
    suma = 0
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

Zad_3()
