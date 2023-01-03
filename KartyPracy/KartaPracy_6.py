print("KARTA PRACY 6")
print()

print("Zadanie 1")

a1 = int(input("A: "))
b1 = int(input("B: "))
c1 = int(input("C: "))
geo = "Nie"
art = "Nie"
ros = "Nie"
mal = "Nie"

if a1 < b1 and b1 < c1:
    ros = "Tak"
    if c1 - b1 == b1 - a1:
        art = "Tak"
    if c1 / b1 == b1 / a1:
        geo = "Tak"
elif a1 > b1 and b1 > c1:
    mal = "Tak"
    if a1 - b1 == b1 - c1:
        art = "Tak"
    if a1 / b1 == b1 / c1:
        geo = "Tak"
elif a1 == b1 and b1 == c1:
    art = "Tak"
else:
    exit
print(f"Rosnąco: {ros}\nMalejąco: {mal}\nArytmetyczny: {art}\nGeometryczny: {geo}")
print()       
 
print("Zadanie 2")

suma2 = 0

for i in range(100, 1000):
    if i % 8 == 0 and i % 16 != 0:
        suma2 += i
print(f"Suma: {suma2}")
print()

print("Zadanie 3")

nw = 0
suma3 = 0;

for w in range(10, 100):
    if w % 7 == 0:
        nw = w
print(f"Największa liczba 2-cyfrowa podzielna przez 7 to {nw}.")

for i in range(1000, 10000):
    if i % nw == 0:
        suma3 += i
print(f"Suma: {suma3}")
print()

print("Zadanie 4")

ilosc4 = 0

for i in range(10, 100):
    if (i // 10) > 2 * (i % 10):
        ilosc4 += 1
print(ilosc4)
print()

print("Zadanie 5")

ilosc5 = 0
suma5 = 0

for i in range(100, 1000):
    if i // 100 > ((i // 10) % 10) + (i % 10):
        ilosc5 += 1
        suma5 += i
print(f"Ilość: {ilosc5}\nSuma: {suma5}")
print()

print("Zadanie 6")

n6 = int(input("Ile chcesz liczb: "))
suma6 = 0
p5 = 0

for i in range(10, 100):
    if i % 19 == 0:
        p5 += 1
        suma6 += i
        if p5 == n6:
            break
print(suma6)
print()

print("Zadanie 7")

n7 = int(input("Ile chcesz liczb: "))
suma7 = 0
p7 = 0

for i in range(1000, 100, -1):
    if i % 37 == 0:
        print(i)
        p7 += 1
        if p7 == n7:
            break
print()

print("Zadanie 8")

n8 = int(input("Ile liczb: "))
suma8 = 0
l8 = 2

for i in range(n8):
    if l8 % 2 == 0:
        suma8 += l8
        print(f"{l8}", end='')
    else:
        suma8 -= l8
        print(f" - {l8} + ", end='')
    l8 += 3
print(f" = {suma8}")
print()

print("Zadanie 9")

n9 = int(input("Ile liczb: "))
iloczyn9 = 1
poteda = 1

for i in range(n9):
    iloczyn9 *= pow(-2, poteda)
    print(pow(-2, poteda), "* ", end='')
    poteda +=1
print("=", iloczyn9)
print()

print("Zadanie 10")

n10 = int(input("Ile liczb silni: "))
suma10 = 0

for i in range(1, n10 + 1):
    silnia = 1
    for j in range(1, i + 1):
        silnia *= j
    suma10 += silnia
print(f"Suma silni: {suma10}")
print()

print("Zadanie 11")

n11 = int(input("Ciąg niebanalny. Ile elementów: "))
suma11 = 0
d11 = 1
q11 = 0

for i in range(1, n11 + 1):
    q11 = i * i
    suma11 += d11 / q11
    print(f"{d11}/{q11} + ")
    d11 += 2
print("Suma", round(suma11, 2))
print()

print("Zadanie 12")

n12 = int(input("Ciąg niebanalny 2. Ile liczb: "))
suma12 = 0
suma12_q = 0
suma12_d = 0

for i in range(1, n12 + 1):
    suma12_d += i * 2 - 1
    suma12_q += i * i
print(f"{suma12_d} / {suma12_q} = {round(suma12_d / suma12_q, 2)}")
print()


print("Zadanie 13")

n13 = int(input("Ciąg wymagający. Ile liczb: "))
suma13 = 0
temp13 = 0
q13 = 3

for i in range(1, n13 + 1):
    suma13 += i * 2 / q13
    print(f"{i * 2}/{q13} + ", end="")
    temp13 += i
    q13 += temp13 * 6 + 1
print(f"... = {round(suma13,2)}")
print()
