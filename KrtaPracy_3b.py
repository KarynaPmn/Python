print("Zadanie 1")
for i in range(1, 32):
    print(i, "listopada 2022")

print("Zadanie 2")
n2 = int(input("Podaj liczbę: "))
for i in range(0, n2*2):
    if i % 2 == 1:
        print(i*i)

print("Zadanie 3")
for i in range(1000,10000):
    if i % 379 == 0:
        print(i)

print("Zadanie 4")
for i in range(100,1000):
    if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
        print(i)

print("Zadanie 5")
n5 = int(input("Ile chcesz podać liczb?: "))
suma5 = 0
for i in range(0,n5):
    l = int(input("Podaj liczbę:"))
    suma5 += l
print("Suma podanych liczb wynosi:", suma5)

print("Zadanie 6")
k6 = int(input("Podaj liczbę:"))
suma6 = 0
for i in range(0, k6):
    if i % 2 == 0:
        suma6 += i
print(suma6)

print("Zadanie 7")
m7 = int(input("Podaj liczbę dwucfrową:"))
suma7 = 0
if m7 >= 10 and m7 < 100:
    for i in range(10,m7):
        if i % 2 == 1:
            suma7 += i
    print(suma7) 
else:
    print("Liczba nie jest dwucyfrowa.")

print("Zadanie 8")
W = int(input("Podaj kwotę: "))
L = int(input("Podaj lata inwestycji:"))
wart = W
wartM = 0
for i in range(0, L * 12):
    wartM = wart * 0.06 * (1/12)
    wart += wartM
print("Wartość inwestycji wynosi", round(wart, 2), "zł.")

print("Zadanie 9")
n9 = int(input("Podaj ile chcesz liczb:"))
k9 = 21
suma9 = 0
for i in range(0,n9):
    print(k9)
    suma9 += k9
    k9 += 100


from math import sqrt

print("Zadanie 10")
for i in range(1,100):
    sqrt(i) % i == 0

from math import sqrt


print("Zadanie 10")
for i in range(1, 1000):
    if i % 10 == sqrt(i):
        print(i)
    elif i % 100 == sqrt(i):
        print(i)
    elif i % 1000 == sqrt(i):
        print(i)
