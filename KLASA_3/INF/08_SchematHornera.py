def SchematHornera_1(W, x):
    stopienWielomianu = len(W) - 1
    wynik = W[0]
    potega = 1

    for i in range(1, stopienWielomianu + 1):
        potega *= x
        wynik += W[i] * potega

    return wynik

def SchematHorneraOdwroconaWersja_1(W, x):
    stopienWielomianu = len(W) - 1
    wynik = W[stopienWielomianu]
    potega = 1

    for i in range(stopienWielomianu - 1, -1, -1):
        potega *= x
        wynik += W[i] * potega

    return wynik

# Nie działa przwidłowo!!! do zadania 2
def SchematHornera_2(W, x):
    stopienWielomianu = len(W) - 1
    y = W[stopienWielomianu]

    for i in range(stopienWielomianu, 1):
        y = x * y + W[i]

    return y

def SchematHorneraOdwroconaWersja_2(W, x):
    stopienWielomianu = len(W) - 1
    y = W[0]

    for i in range(1, stopienWielomianu + 1):
        y = x * y + W[i]

    return y

# # Nie działa przwidłowo!!! do zadania 3
def SchematHorneraReku(W, x):
    stopienWielomianu = len(W) - 1

    if stopienWielomianu == 0:
        return W[0]
    return x * SchematHorneraReku(W[1:], x) + W[0]

# Zad 1
def Zad_1():
    Wspolczynniki = list(map(int, input("Podaj: ").split(" ")))
    x = int(input("Podaj x: "))

    print(SchematHornera_1(Wspolczynniki, x))

# Zad 2
def Zad_2():
    Wspolczynniki = list(map(int, input("Podaj: ").split(" ")))
    x = int(input("Podaj x: "))

    print(SchematHornera_2(Wspolczynniki, x))

# Zad 3
def Zad_3():
    Wspolczynniki = list(map(int, input("Podaj: ").split(" ")))
    x = int(input("Podaj x: "))

    print(SchematHorneraReku(Wspolczynniki, x))

# Zad 5
def Zad_5_1():
    Wspolczynniki = list(map(int, input("Podaj: ").split(" ")))
    x = int(input("Podaj x: "))

    print(SchematHorneraOdwroconaWersja_1(Wspolczynniki, x))

def Zad_5_2():
    Wspolczynniki = list(map(int, input("Podaj: ").split(" ")))
    x = int(input("Podaj x: "))

    print(SchematHorneraOdwroconaWersja_2(Wspolczynniki, x))

# Zad 6
def Zad_6():
    liczbaBinarna = input("Podaj liczbę binarną: ")

    print(BinarnyNaDziesietnySchematHornera(liczbaBinarna))

def BinarnyNaDziesietnySchematHornera(x):
    wynik = 0

    for i in range(len(x)):
        wynik = wynik * 2 + int(x[i])

    return wynik

# Zad 7
def Zad_7():
    liczba = input("Podaj liczbę w systemie o podstawie: ")
    podstawa = int(input("Podaj podstawę: "))

    print(LiczbaPodstawieNaDziesietnySchematHornera(liczba, podstawa))

def LiczbaPodstawieNaDziesietnySchematHornera(x, podstawa):
    wynik = 0

    for i in range(len(x)):
        wynik = wynik * podstawa + int(x[i])

    return wynik
