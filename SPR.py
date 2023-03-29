#  1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# n_1 = str(input('Podaj napis: '))
# print(f"{n_1[0]} i {n_1[-1]}" )

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# n_2 = input('Wpisz: ')
# print(n_2[1:-1])
# print(n_2[1 : len(n_2) - 1])
# for i in range(1, len(b) - 1):
# 	print(n_2, end=' ')

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca

# c = input()
# print(c[-1:-5:-1])
# print(c[:-5:-1])

# for i in range(len(c) - 1):
# 	print(c, end=" ")

# C =list(c)
# C.reverse()
# c = "".join(C)
# print(c[:4])

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis

# d = input()
# s = 0

# for i in d:
# 	s += ord(i)
# print(s)

# 5. Policz ile we wpisanym napisie jest liter A.

# e = input()
# s = 0

# for i in e:
# 	if i == "a":
# 		s += 1

# print(s)

# 6. Podaj dominującą literkę we wpisanym napisie. Niech to będzie tylko jedna literka.

# n = input("Wpisz: ")
# maksi = 0
# literka = ""

# for i in n:
# 	if n.count(i) > maksi:
# 		maksi = n.count(i)
# 		literka = i

# print(literka, maksi)

# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

def czyJestPierwszyNiezerowy(L):
	for x in L:
		if 0 < L.count(x) < max(L):
			return True
	return False

g = input("Wpisz: ")
K = [0] * 100
for x in g:
	K[ord(x)] += 1
print(K)
domikand = max(K)

if sum(K) == max(K):
	print(f"Dominanta: {chr(K.index(max(K)))}")
elif not czyJestPierwszyNiezerowy(K):
	print("Brak dominanty")
else: 
	D = []
	for x in range(len(K)):
		if K[x] == max(K):
			D.append(chr(x))
	print("Dominanty:", ", ".join(D)) 

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
# TIP: h[i:i+2] == "LA"

# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie ułamkowy to zaokrąglij średnią w dół) <można zrobić wersję w górę>

# 10. Wypisz literki, których nie ma w napisie

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)
# TIP: funkcja palindrom[]