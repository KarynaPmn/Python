# Nie zakończone !!!
def NajdluzszyWspolnyPodciag(X, Y):
    n = len(X)
    m = len(Y)
    D = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        D[i][0] = 0
    for j in range(1, m + 1):
        D[0][j] = 0
    for i in range(1, n):
        for j in range(1, m):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])

    i = n
    j = m
    k = D[n][m]
    N = [[0 for j in range(m + 1)] for i in range(n + 1)] # zawiera znaki najdłuższego wspólnego podciągu w odpowiedniej kolejności.
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            N[k] = X[i - 1]
            k -= 1
            i -= 1
            j -= 1
        elif D[i - 1][j] >= D[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return D[n][m] # długość najdłuższego ciągu

def Zad_2():
    # X = list(map(int, input("Podaj 1 ciąg liczb całkowitych: ").split()))
    # Y = list(map(int, input("Podaj 2 ciąg liczb całkowitych: ").split()))

    NajdluzszyWspolnyPodciag([1, 2, 3, 4], [2, 3, 4, 5])

Zad_2()

###
def najdluzszy_wspolny_podciag(X, Y):
    # D = [[0] * (m + 1) for _ in range(n + 1)]
    n = len(X)
    m = len(Y)
    D = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])

    i = n
    j = m
    k = D[n][m]
    n = ""
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            n = X[i - 1]+n
            k = k - 1
            i -= 1
            j -= 1
        elif D[i - 1][j] >= D[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return n

def najdluzszy_wspolny_podciag_wyraz(X, Y):
    text = ""
    n = len(X)
    m = len(Y)
    D = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + 1
            else:
                D[i][j] = max(D[i - 1][j], D[i][j - 1])

    i = n
    j = m
    k = D[n][m]
    n = ""
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            n = X[i - 1]+n
            k = k - 1
            i -= 1
            j -= 1
        elif D[i - 1][j] >= D[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return n

def Zad_6():
    plik = open("pary.txt", "r")
    # n = int(plik.readlines()) ???
    # print(n)
    pary = [0] * 4
    najdluzszyWspolnyPodciag = [0] * 4
    najPod = 0

    for i in range(4):
        T = list(map(str, plik.readline().split()))
        pary[i] = T

        wynik = najdluzszy_wspolny_podciag(T[0], T[1])
        najdluzszyWspolnyPodciag[i] = wynik
        if (wynik > najdluzszyWspolnyPodciag[najPod]):
            najPod = i
    plik.close()

    print(pary[najPod])

# Nie zakończone
# def Zad_7():
#     text_1 = print("Podaj pierwsze słowo: ")
#     text_2 = print("Podaj drugie słowo: ")
#
#     print(najdluzszy_wspolny_podciag_wyraz(text_1, text_2))

Zad_6()
