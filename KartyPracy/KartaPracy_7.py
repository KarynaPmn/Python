import random


print("KARTA PRACY 7")

print()
print()

T = []

for i in range(40):
    T.append(random.randint(10, 99))
print(T)

print()
print()

# 1
print(f"1) Maksimum: {max(T)}")

# 2
maksi = 0
for i in range(40):
    if T[i] > maksi:
        maksi = T[i]
print(f"Maksimum: {maksi}")

# 1
print(f"2) Mini: {min(T)}")

# 2
mini = maksi

for i in range(40):
    if mini > T[i]:
        mini = T[i]
print(f"Mini: {mini}")

# 1
print(f"3) Rozpiętość tablicy: {max(T) - min(T)}")

# 2

print(f"Rozpiętość tablicy: {maksi - mini}")

# 1
T.sort()
print(f"4) Vice-maksymalny: {T[38]}")

# 2
v_maks = 0

for k in range(len(T)):
    if v_maks < T[k] and maksi > T[k]:
        v_maks = T[k] 
print(f"Vice-maksimum: {v_maks}")

# 1
print(f"5) Vice-minimalny: {T[1]}")

# 2
v_mini = maksi

for i in range(len(T)):
    if v_mini > T[i] and mini < T[i]:
        v_mini = T[i]
print(f"Vice-minimum: {v_mini}")
        
# 1 
print(f"6) Maksymalny element w tablicy występuje {T.count(max(T))} razy.")

# 2
ile_maks = 0
for i in range(len(T)):
    if maksi == T[i]:
        ile_maks += 1
print(f"Maksymalny element występuje {ile_maks} razy.")

# 1
print(f"7) Minimalny element występuje {T.count(min(T))} razy.")

# 2

ile_mini = 0

for i in range(len(T)):
    if mini == T[i]:
        ile_mini += 1
print(f"Minimalny element występuje {ile_mini} razy.")


n = int(input("Wybież liczbę: "))

# 1
print(f"8) Podana przez ciebie liczba występuje {T.count(n)} razy.")

# 2
ile_n = 0
for i in range(len(T)):
    if n == T[i]:
        ile_n += 1
print(f"Podany element występuje {ile_n} razy.")

# 1
print(f"9) Średnia: {round(sum(T) / 40, 1)}")

# 2
suma = 0
for i in range(len(T)):
    suma += T[i]
print(f"Średnia tablicy wynosi { round(suma /len(T), 1)}")

# 1
P = []
for i in range(0, 40, 2):
    P.append(T[i])
print(f"10) Suma elementów: {sum(P)}")

# 2

suma_parzystych = 0
for i in range(0, len(T), 2):
    suma_parzystych += T[i]
print(f"Suma elementów {suma_parzystych}")

# 1
NP = []
for i in range(1, len(T), 2):
    NP.append(T[i])
print(f"11) Średnia liczb o nieparzystych indeksach: {sum(NP) / len(NP)}")

# 2
suma_nieparzystych = 0
np = 0
for i in range(1, len(T), 2):
    np += 1
    suma_nieparzystych += T[i]
print(f"Średnia elementów o nieparzystych indeksach {suma_nieparzystych / np}")

# 1
ile_element_1 = 0
for i in range(len(T)):
    if T.count(T[i]) == 1:
        ile_element_1 += 1
print(f"12) Ilość niepowtarzających się elementów: {ile_element_1}")

# 2
ile_element_2 = 0
for i in range(len(T)):
    ile_element = 0
    for j in range(len(T)):
        if T[j] == T[i]:
            ile_element += 1
    if ile_element == 1:
        ile_element_2 += 1
print(f"Ilość niepowtarzających się elementów: {ile_element_2}")

# 1
E = []
for i in range(10, 100):
    if i not in T:
        E.append(i)
print(f"13) Brakujące elementy w tablicy: {E}")

print()

# 2
for i in range(10, 100):
    if i in T:
        continue
    else:
        print(i, end=" ")

print()

# 1
ile_element_usun_1 = 0
for i in range(len(T)):
    if T.count(T[i]) != 1:
        ile_element_usun_1 += 1
print(f"14) Trzeba usunąć {ile_element_usun_1} aby zostały tylko unikalne wartości.")

# 2
ile_element_usun_2 = 0
for i in range(len(T)):
    element = 0
    for j in range(len(T)):
        if T[i] == T[j]:
            element += 1
    if element != 1:
        ile_element_usun_2 += 1
print(f"Trzeba usunąć {ile_element_usun_2} aby zostały tylko unikalne wartości.")
