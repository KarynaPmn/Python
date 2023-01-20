x = list(range(5))
for item in x:
	print(item)

	for item2 in range(4):
		print(item2)

print(len(x))

 for i in range(len(x)):
 	print(x[i])

# DEKLARACJA LISTY I ITERACJA  PO LIŚCIE

 L = [3, 5, 8, 13, 17, 27]

for elem in L:
	print(elem, end=" ")
print("\n")

for i in range(len(L)):
	print(L[i], end=" ")

## FUNKCJE SPECJALNE NA TABLICACH
K = [4, 7, 5, 7, 3, 3, 2, 8, 7]
print(K)

#apend() - dodaje element do listy
K.append(3)
print(K)

#count() - zwraca ile jest elementów
print(K.count(7))

#index() - zwraca gdzie jest pierwszy element
print(K.index(7))

#insert() - wstawia element do listy pod określonym indeksem.
K.insert(2, 4)
print(K)

#JAK WSTAWIĆ 4 NA KONIEC LISTY?
K.insert(len(K), 4) # lub po prostu append()
print(K)

#pop() - domyślnie usuwa ostatnią
K.pop()
print(K)

#reverse() - odwraca elementy listy
K.reverse()
print(K)

#sort(reverse = true) - true to malejąco
K.sort()
print(K)

# ZADANIE 1. USUŃ WSZYSTKIE 7 Z LISTY (remove, pop i index, count)

# SPOSUB 1
for i in range(K.count(7)):
	K.remove(7)
print(K)
#  SPOSUB 2 
for i in range(K.count(7)):
	K.pop(K.index(7))
print(K)

## ZADANIE 2. POSZUKAM MAKSA W 2 METODAMI

# SPOSÓB 1
print(max(K))

# SPOSÓB 2
maksik = K[0]
for i in K:
	if i > maksik:
		maksik = i
print(maksik)

# SPOSÓS 3. PSEUDOKOD!
maksik = K[0]
for i in range(len(K)):
	if K[i] > maksik:
		maksik = K[i]
print(maksik)

## ZWRACA Z LISTY
L = [3, 7, 2, 1, 5, 4, 2, 4, 8, 6]
print(L[1:4]) # [7, 2, 1]]
print(L[:3]) # [3, 7, 2]
print(L[7]) # 4
print(L[7:]) # [4, 8, 6]
print(L[5 :: 2]) # [4, 4, 6]
print(L[5 : 3]) # nic []
print(L[5 : 3 : -1]) # [4, 5]
print(L[: 2 : -3]) # [6, 2, 1]
print(L[::-3]) # [6, 2, 1, 3]


