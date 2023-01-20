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
print(f"1) Maksik: {max(T)}")

# 2
maksi = 0
for i in range(40):
    if T[i] > maksi:
        maksi = T[i]
print(f"Maksik: {maksi}")

# 1
print(f"2) Mini: {min(T)}")

# 2
mini = 100

for i in range(40):
    if mini > T[i]:
        mini = T[i]
print(f"Mini: {mini}")

# 1
print(f"3) {max(T) - min(T)}")

# 2


T.sort()
print(f"4) Vice-maksymalny: {T[-2]}")

print(f"5) Vice-minimalny: {T[-39]}")

print(f"6) Maksymalny element w tablicy występuje {T.count(max(T))} razy.")

print(f"7) Minimalny element występuje {T.count(min(T))} razy.")

n = int(input("Wybież liczbę: "))
print(f"8) Podana przez ciebie liczba występuje {T.count(n)} razy.")

print(f"9) Średnia: {round(sum(T) / 40, 1)}")

for i in range(0, 40, 2):
    print(f"10) Suma elementów: {sum(T[i])}")

