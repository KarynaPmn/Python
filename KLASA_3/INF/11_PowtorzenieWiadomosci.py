def Zad_2():
    wsp = list(map(int, input("Podaj ciąg liczb: ").split())) # 11 -2 3 3
    x = int(input("Podaj x: ")) # 2
    n = len(wsp)
    stopien = n - 1
    w = wsp[n - 1]

    for i in range(n - 2, -1, -1):
        w = w * x + wsp[i]

    print(w) # 43

def Zad_3():
    Ciag = list(map(int, input("Podaj ciąg: ").split(' ')))

    czyRosnący = True
    for i in range(len(Ciag) - 1):
        if (Ciag[i] > Ciag[i + 1]):
            czyRosnący = False
            break
    
    if (czyRosnący):
        print("tak")
    else:
        print("nie")

def Zad_4():
    plik = open("liczby.txt", "r")
    ciag = list(map(int, plik.readline().split()))
    n = len(ciag)
    dl = 0
    dl_max = 0

    for i in range(1, n):
        if (ciag[i] >= ciag[i - 1]):
            dl += 1
        else:
            if (dl > dl_max):
                dl_max = dl
            dl = 1
    if (dl > dl_max):
        dl_max = dl

    plik.close()
    print(dl_max)

def Zad_5():
    with open("ciag.txt", "r") as file:
        ciag = list(map(int, file.read().split()))

    maxSuma = ciag[0]
    n = len(ciag)
    for pocz in range(n):
        suma = sum(ciag[pocz:pocz + 3])
        if (suma > maxSuma):
            maxSuma = suma
    print(maxSuma)

def Zad_6():
    with open("ciag.txt", "r") as file:
        ciag = list(map(int, file.read().split()))

    maxSuma = ciag[0]
    n = len(ciag)
    for pocz in range(n):
        for dl in range(1, n - pocz + 1):
            suma = sum(ciag[pocz:pocz + dl])
            if (suma > maxSuma):
                maxSuma = suma
    print(maxSuma)

def Zad_7():
    plik = open("Sprawdzian_2/ciagi.txt", "r")
    ciag = list(map(int, plik.read().split()))

    n = len(ciag)
    for pocz in range(n - 2):
        suma = sum(ciag[pocz : pocz + 3])
        if (suma == 10):
            print(ciag[pocz : pocz + 3])

    plik.close()
