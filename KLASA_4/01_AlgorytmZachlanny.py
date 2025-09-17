plik = open("nominaly.txt", "r")
nominaly = list(map(int, plik.readline().split()))
plik.close()

def Zad_1(kwota):
    for nominal in nominaly:
        ile = 0
        ile = kwota // nominal
        kwota = kwota % nominal

        if (ile > 0):
            print(nominal, " x ", ile)


def Zad_4():
    N = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V",
         4: "IV", 1: "I"}
    l = int(input("Podaj liczbę: "))

    for nominal in N:
        ile = 0
        ile = l // nominal
        l = l % nominal

        if (ile > 0):
            print(N[nominal], " x ", ile)

def Zad_5():
    N = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    liczbaRzymska = input("Podaj liczbę rzymską: ")
    liczbaD = 0

    for i in range(len(liczbaRzymska) - 1):
        pierwsza = liczbaRzymska[i]
        nastepna = liczbaRzymska[i + 1]

        if (N[pierwsza] < N[nastepna]):
            liczbaD -= N[pierwsza]
        else:
            liczbaD += N[pierwsza]

    liczbaD += N[liczbaRzymska[-1]]

    print(liczbaD)

