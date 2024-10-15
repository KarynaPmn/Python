# 1. Dzielniki liczby
def DzielnikiLiczby_1(n):
    for i in range(1, n - 1):
        if n % i == 0:
            print(i, end=" ")
    print()

def DzielnikiLiczby_2(n):
    L = []
    i = 1
    while i * i < n:
        if n % i == 0:
            L.append(int(i))
            L.append(int(n//i))
        i += 1
    if i * i < n:
        L.append(i)
    L.sort()
    print(L)
    print()

def CzyLiczbaPierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 2. Faktoryzacja -- rozkład na czynniki pierwsze
def Faktoryzacja(n):
    czynnikPierwszy = 2
    while n > 1:
        if n % czynnikPierwszy == 0:
            print(czynnikPierwszy, end=" ")
            n //= czynnikPierwszy
        else:
            czynnikPierwszy += 1

# 3. Liczby doskonałe -- jest równa sumie swoich dzielników właściwych (czyli mniejszych od tej liczby). 
# 6 = 1+2+3
# 28 = 1+2+4+7+14
def LiczbyDoskonale(n):
    sumaDzielnikow = 0
    for i in range(1, n):
        if n % i == 0:
            sumaDzielnikow += i
    
    if sumaDzielnikow == n:
        print("Tak")
    else:
        print("Nie")

# 4. Liczby bliźniacze -- są liczbami pierwszymi i ich różnica wynosi 2, np. liczby 5 i 7 oraz 11 i 13 są liczbami bliźniaczymi, a 7 i 9 nie są bliźniacze, bo 9 nie jest liczbą pierwszą.
def LiczbyBlizniacze():
    userNumberA, userNumberB = map(int, input("Podaj dwie liczby po przecinku: ").split(" "))  
    if CzyLiczbaPierwsza(userNumberA) and CzyLiczbaPierwsza(userNumberB) and abs(userNumberA - userNumberB) == 2:
        print("Tak")
    else:
        print("Nie")
        
# 5. Liczby zaprzyjaźnione -- są różne oraz suma dzielników właściwych liczby a jest równa liczbie b oraz suma dzielników właściwych liczby b jest równa liczbie a.
# Dzielniki liczby 284: 1, 2, 4, 71, 142
# Dzielniki liczby 220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
# 220 = 1 + 2 + 4 + 71 + 142
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110
# Kolejna para liczb zaprzyjaźnionych: 1184 i 1210
def LiczbyZaprzyjaznione():
    userNumberA, userNumberB = map(int, input("Podaj dwie liczby po przecinku: ").split())
    
    sumaDzielnikowA = 0
    for i in range(1, userNumberA):
        if userNumberA % i == 0:
            sumaDzielnikowA += i
            print(i, end=" ")
    print(sumaDzielnikowA)

    sumaDzielnikowB = 0
    for i in range(1, userNumberB):
        if userNumberB % i == 0:
            sumaDzielnikowB += i
            print(i, end=" ")
    print(sumaDzielnikowB)

    if sumaDzielnikowA == userNumberB and sumaDzielnikowB == userNumberA:
        print("Tak")
    else:
        print("Nie")

# 6. Liczby Smitha -- liczba naturalna złożona, której suma cyfr jest równa sumie cyfr czynników pierwszych. 
# Liczba 202 -- 2 + 0 + 2 = 4 i czynniki pierwsze 202 = 2 · 101 suma cyfr obu czynników wynosi 2+1+0+1=4
def SumaCyfrCzynnikowPierwszych(n):
    sumaCzynnikowPierwszych = 0
    czynnikPierwszy = 2
    while n > 1:
        while n % czynnikPierwszy == 0:
            sumaCzynnikowPierwszych += SumaCyfrLiczby(czynnikPierwszy)
            n //= czynnikPierwszy
        czynnikPierwszy += 1
    return sumaCzynnikowPierwszych

def SumaCyfrLiczby(n):
    sumaCyfrLiczby = 0
    while n > 0:
        sumaCyfrLiczby += n % 10
        n //= 10
    return sumaCyfrLiczby

def LiczbySmitha(n):
    print(SumaCyfrLiczby(n), " ", SumaCyfrCzynnikowPierwszych(n))
    if SumaCyfrLiczby(n) == SumaCyfrCzynnikowPierwszych(n) and not CzyLiczbaPierwsza(n):
        print("Tak")
    else:
        print("Nie")
