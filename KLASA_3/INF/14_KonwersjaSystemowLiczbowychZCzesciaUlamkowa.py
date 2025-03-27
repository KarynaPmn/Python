# --- Zadanie 1. ---
# Zamień liczby rzeczywiste w zapisie binarnym na system dziesiętny.
#     a) 101,01012 = 1*22 + 0*21 + 1*20 + 0*2-1 + 1*2-2 + 0*2-3 + 1*2-4  = 2 + 0,25
#     b) 10111,00112 = 23 + 3/(24) = 23 + 3/16 = 23,187510

# --- Zadanie 2 ---
# Zamień podane liczby dziesiętne na system binarny.
#     a) 43,2510 =  101011,012
#       43 : 2 = 21   r1
#       21 : 2 = 10   r1
#       10 : 2 = 5    r0
#       5  : 2 = 2    r1
#       2  : 2 = 1    r0
#       1  : 2 = 0    r1 → od tego miejsca do góry

#       0,25 * 2 = 0,5   → cyfra 0 po przecinku czytamy od tego miejsca w dół
#       0,5  * 2 = 1,0   → cyfra 1

#     b) 21,37510 = 11001,0(0011)2
#       21 : 2 = 10 r1
#       10 : 2 = 5   r0
#       5  : 2 = 2   r1
#       2  : 2 = 1   r0
#       1  : 2 = 0   r1
      
#       0,1 * 2 = 0,2   → 0
#       0,2 * 2 = 0,4   → 0
#       0,4 * 2 = 0,8   → 0
#       0,8 * 2 = 1,6   → 1
#       0,6 * 2 = 1,2   → 1
#       0,2 * 2 = 0,4   → 0

#     c) 34,812510
#     d) 25,110
#     e) 13,410

# --- Zadanie 3 ---
# Zamień podane liczby na system binarny, a następnie z binarnego na ósemkowy i szesnastkowy.
#     a) 53210 = 1 000 010 1002 = 10248 = 10 0001 01002 = 21416
#     b) 8410 = 1 010 1002 = 1248 = 101 01002 = 5416
#     c) 14910

# --- Zadanie 4 ---
# Zamień liczbę 2103232014 na system heksadecymalny.
#     2103232014 = 1 10 32 32 014 = 24EE116

# --- Zadanie 5 ---
# Zamień liczbę EA19C037D16 na system o podstawie 4.
#     EA19C037D16 = 3222012130000313314

######################################################

def BinToDec(bin):
    czesci = bin.split(',')
    calkowiata = czesci[0]
    ulamek = czesci[1]
    dl_calk = len(calkowiata)
    wynik = 0
    odwrocona = calkowiata[:: -1]

    for i in range(dl_calk):
        if (odwrocona[i] == "1"):
            wynik += 2**(i)

    dl_ulam = len(ulamek)
    for i in range(dl_ulam):
        if (ulamek[i] == "1"):
            wynik += 2**(-i - 1)

    print(wynik)


def Zad_1():
    bin = input("Podaj bin: ")
    BinToDec(bin)


Zad_1()
