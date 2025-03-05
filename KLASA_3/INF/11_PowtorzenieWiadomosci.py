def Zad_2():
    wsp = list(map(int, input("Podaj ciąg liczb: ").split())) # 11 -2 3 3
    x = int(input("Podaj x: ")) # 2
    n = len(wsp)
    stopien = n - 1
    w = wsp[n - 1]

    for i in range(n - 2, -1, -1):
        w = w * x + wsp[i]

    print(w) # 43

def Zad_4():
    plik = open("liczby.txt", "r")
    ciag = list(map(int, plik.readline().split()))
    n = len(ciag)
    dl = 0
    dl_max = 0

    for i in range(1, n):
        if (ciag[i] > ciag[i - 1]):
            dl += 1
        else:
            if (dl > dl_max):
                dl_max = dl

    plik.close()
    print(dl_max)

Zad_4()
