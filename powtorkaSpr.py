#### Czy pierwsza podana liczba ####

n = int(input("Wpisz:"))

def CzyPierwsza(n):
    for i in range(2, int(n * 0.5 + 1)):
        if (n % i == 0): 
            return False
    return True


#### Generator liczb pierwszych####

for i in range(10, 100):
    flaga = 1
    for j in range(2, int(i * 0.5) + 1):
        if (i % j == 0):
            flaga = 0
    if (flaga == 1):
        print(i)

#### Generator początkowych k liczb pierwszych #####

k = int(input("Ile liczb chcesz: "))
t = 0
i = 2

while t != k:
    if CzyPierwsza(i) == True:
        print(i, end=" ")
        t += 1
    i += 1

#### Cezar ####

for i in range(65, 90):
    print(chr(i), end=" ")

N = input()
W = ""

print()

# SPOSÓB 1

for i in range(len(N)):
    W += chr( 65 + (ord(N[i]) - 65 + 3) % 26)
print(W)

# SPOSÓB 2

for i in N:
    if (ord(i) + 3 > 90):
        W += chr(65 + ((ord(i) + 3) - 90))
    else:
        W += chr(ord(i) + 3)
print(W)

#### Hufman ####

W = "ABBCCCDDDDE"
E = ""
ilosc = 1

for i in range(len(W) - 1):
    if (W[i] == W[i + 1]):
        ilosc += 1
    else:
        if (ilosc == 1):
            E += W[i]
        else:
            E += W[i] + str(ilosc)
        ilosc = 1
if (ilosc == 1):
    E += W[-1]
else:
    E += W[-1] + str(ilosc)

print(E)

#### RSA ####

# 1. Liczby pierwsze

a = 11
b = 13

# 2. Funkcja Eukidesa i znalezienie n

eukides = (a - 1) * (b - 1)
n = a * b

print("Eukides: ", eukides)
print("n: ", n)

# 3. Klucz publiczny

def NWD(p, d):
    while (p != d):
        if (p > d): p -= d
        if (d > p): d -= p
    return p

for i in range(2, eukides):
    if (NWD(i, eukides) == 1):
        k_publiczny = i
        break

print("Klucz publiczny: ", k_publiczny)

# Klucz prywatny

for i in range(2, n):
    if ((i * k_publiczny) % eukides == 1):
        k_prywatny = i
        break

print("Klucz prywatny: ", k_prywatny)

# Zastosowanie 
# szyfogram = x ** k_publiczny % n
# jawny = szyfogram ** k_prywatny % n

jawny1 = input()
szyfrogram1 = ""

for i in jawny1:
    szyfrogram1 += chr(ord(i) ** k_publiczny % n)
print(szyfrogram1)

szyfrogram2 = input()
jawny2 = ""

for j in szyfrogram2:
    jawny2 += chr(ord(j) ** k_prywatny % n)
print(jawny2)
