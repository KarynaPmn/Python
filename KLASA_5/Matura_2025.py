# Zad. 1.1

def przestaw_rek(n):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    w = 0
    if n > 0:
        w = a + 10*b + 100*przestaw_rek(n)
    else:
        if a > 0:
            w = a + 10*b
        else:
            w = b

    return w

# Zad. 1.3 - iteracyne
def przestaw_1(n):
    wynik = 0
    mnoznik = 1

    while n > 0:
        para = n % 100
        n //= 100

        if para < 10:
            odwrocona = para
        else:
            a = para // 10
            b = para % 10

            odwrocona = b*10 + a

        wynik = wynik + odwrocona*mnoznik
        mnoznik = mnoznik*100

    return wynik

# Zad. 1.3 - tylko operacje arytmetyczne
def przestaw_2(n):
    wynik = 0
    mnoznik = 1

    while n > 9:
        para = n % 100
        n //= 100

        a = para // 10
        b = para % 10

        odwrocona = b*10 + a

        wynik = wynik + odwrocona*mnoznik
        mnoznik = mnoznik*100

    if n > 0:
        wynik = wynik + n*mnoznik

    return wynik

# Zad. 2.1
def palindrom(text):
    if text == text[::-1]:
        return True

    return False

def Zad_2_1():
    plik = open("symbole.txt", "r")

    for line in plik:
        line = line.rstrip()
        if palindrom(line):
            print(line)

    plik.close()

# Zad. 2.2
def Zad_2_2():
    plik = open("symbole.txt", "r")
    symbole = []

    for line in plik:
        line = list(line.strip().strip())
        symbole.append(line)

    ile = 0

    srodki = []

    for i in range(1, len(symbole) - 1):
        for j in range(1, len(symbole[1]) - 1):
            srodek = symbole[i][j]

            if (srodek == symbole[i-1][j-1]
                and srodek == symbole[i-1][j]
                and srodek == symbole[i-1][j+1]
                and srodek == symbole[i][j-1]
                and srodek == symbole[i][j+1]
                and srodek == symbole[i+1][j-1]
                and srodek == symbole[i+1][j]
                and srodek == symbole[i+1][j+1]):
                    ile += 1
                    srodki.append((i + 1, j + 1))

    print(ile)
    print(*srodki[0]) # * - usuwa nawiasy
    plik.close()

# Zad 3.2
def zad_3_2():
    plik = open('dron.txt', 'r')
    punkty = []
    x = 0
    y = 0
    ile = 0

    for linia in plik:
        linia = linia.rstrip()
        a, b = linia.split()
        x = x + int(a)
        y = y + int(b)

        punkty.append([x, y])

        # punkt a
        if 0 < x < 5000 and 0 < y < 5000:
            ile += 1

    print(ile)

    # punkt b
    n = len(punkty)
    for i in range(n):
        for j in range(i + 1, n):
            xs = (punkty[i][0] + punkty[j][0]) / 2
            ys = (punkty[i][1] + punkty[j][1]) / 2

            if [xs, ys] in punkty:
                print(f"({punkty[i][0]},{punkty[i][1]}), ({xs},{ys}), ({punkty[j][0]},{punkty[j][1]})")

    plik.close()
    
