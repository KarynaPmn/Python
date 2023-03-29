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
