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
