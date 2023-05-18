# Zadanie 1
print("Zadanie 1")
napis_1 = "szkola"
for i in range(len(napis_1) + 1):
	print(" " * (len(napis_1) - i), napis_1[:i])
print()

# Zadanie 2
print("Zadanie 2")
napis_2 = "beuunneanno"
ile_par = 0
for i in range(len(napis_2) - 1):
	if napis_2[i] == napis_2[i + 1]:
		ile_par += 1
print(ile_par)
print()

# Zadanie 3
print("Zadanie 3")
napis_3 = "ANNA"
T = [0] * 100
for x in napis_3:
	T[ord(x)] += 1
ile_roznych = 0 
for a in T:
	if a != 0:
		ile_roznych += 1
print(ile_roznych)
print()

# Zadanie 4
print("Zadanie 4")
napis_4 = "KMLAAERKNLSA"
for i in range(3):
	print(napis_4[i::3])
