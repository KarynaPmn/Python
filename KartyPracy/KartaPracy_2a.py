# print("KARTA PRACY 2A")
# print("Zadanie 1\nSprawź czy suma dwóch podanych liczb jest parzysta.")
# a1 = int(input("Podaj pierwszą liczbę: "))
# b1 = int(input("Podaj drugą liczbę: "))

# if (a1 + b1) % 2 == 0:
#     print("Tak. Suma liczb jest parzysta.")
# else:
#     print("Nie. Suma podanych liczb nie jest parzysta.")

# print("Zadanie 2\nSprawdź czy średnia arytmetyczna dwóch podanych licb jest większa od jej średniej geometrycznej.")
# a2 = int(input("Podaj pierwszą liczbę: "))
# b2 = int(input("Podaj drugą liczbę: "))

# if (a2 + b2) / 2 > (a2 * b2)**(1 / 2):
#     print("Tak. Średnia arytmetyczna wpisanych liczb jest większa.")
# else:
#     print("Nie. Średnie geometryczna wpisanych liczb jest większa.")

# print("Zadanie 3\nPodaj 3 liczby całkowite. Dwie z nich muszą być sobie równe.")
# k = int(input("Podaj pierwszą liczbę: "))
# l = int(input("Podaj drugą liczbę: "))
# m = int(input("Podaj trzecią liczbę: "))

# if k == l == m:
#     print("Nie. Trzy podane liczby są sobie równe.")
# elif k == l:
#     print("Tak. Są sobie równe dwie liczby: ", k)
# elif l == m:
#     print("Tak. Są sobie równe dwie liczby: ", l)
# elif m == k:
#     print("Tak. Są sobie równe dwie liczby: ", m)
# else:
#     print("Nie. Żadna z podanych liczb nie jest sobie równa.")

# print("Zadanie 4\nWprowaź 4 różne liczby. Program sprawdzi, która z podanych liczb jest najmniejsza.")
# a4 = int(input("Podaj pierwszą liczbę:"))
# b4 = int(input("Podaj drugą liczbę:"))
# c4 = int(input("Podaj trzecią liczbę:"))
# d4 = int(input("Podaj czwartą liczbę:"))

# if a4 < b4 and a4 < c4 and a4 < d4:
#     print("Tak. Najmniejszą z liczb jest: ", a4)
# elif b4 < a4 and b4 < c4 and b4 < d4:
#     print("Tak. Najmniejszą z liczb jest: ", b4)
# elif c4 < a4 and c4 < b4 and c4 < d4:
#     print("Tak. Najmniejszą z liczb jest: ", c4)
# elif d4 < a4 and d4 < b4 and d4 < c4:
#     print("Tak. Najmniejszą z liczb jest: ", d4)
# else:
#     print("Nie. Przynajniej dwie z podanych liczb są sobie równe.")

# print("Zadanie 5\nWprowax trzy liczby, króre spełniaja nierówność trójkąta.")
# a5 = int(input("Podaj pierwszą liczbę:"))
# b5 = int(input("Podaj drugą liczbę:"))
# c5 = int(input("Podaj trzecią liczbę:"))

# if a5 < b5 + c5 and a5 > b5 - c5 and b5 < a5 + c5 and b5 > a5 - c5 and c5 < a5 + b5 and c5 > a5 - b5:
#     print("Tak. Podane liczby spełniają nierówność trójkąta.")
# else:
#     print("Nie. Podane liczby nie spełniają nierówność trójkąta.")

# print("Zadanie 6\nWprowadź trzy liczby, z których można zbudować trójkąt.")
# a6 = int(input("Podaj pierwszą liczbę:"))
# b6 = int(input("Podaj drugą liczbę:"))
# c6 = int(input("Podaj trzecią liczbę:"))

# if a6**2 == b6**2 + c6**2 or b6**2 == a6**2 + c6**2 or c6**2 == a6**2 + b6**2:
#     print("Tak. Z podanych liczb można zbudować trójkąt prostokątny.")
# elif a6**2 > b6**2 + c6**2 or b6**2 > a6**2 + c6**2 or c6**2 > a6**2 + b6**2:
#     print("Tak. Z podanych liczb można zbudować trójkąt rozwartokątny.")
# elif a6**2 < b6**2 + c6**2 or b6**2 < a6**2 + c6**2 or c6**2 < a6**2 + b6**2:
#     print("Tak. Z podanych liczb można zbudować trójkąt ostrokątny.")
# else:
#     print("Nie. Z podanych liczb nie można zbudować trójkąt.")


