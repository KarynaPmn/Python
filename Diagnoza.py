### Diagnoza INF ###

### WSTĘP ###

# 1. Oblicz sumę liczb 3-cyfrowych
suma_1 = 0
for i in range(100, 1000):
	suma_1 += i
print(f"1. {suma_1}")

# 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
suma_2 = 0
ilosc_2 = 0
for i in range(10,100):
	if i % 6 == 0:
		suma_2 += i
		ilosc_2 += 1
print(f"2. {suma_2} i {ilosc_2}")

# 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
import random
T = [random.randint(1000, 10000) for i in range(5)]
maksi = 0
for i in range(len(T)):
	if (T[i] > maksi):
		maksi = T[i]
print(f"3. {T}\n  Max: {maksi}")

# 4. Podaj sumę cyfr w dowolnej liczbie
suma_4 = 0
n_4 = 101010
while n_4 > 0:
	suma_4 += (n_4 % 10)
	n_4 //= 10
print(f"4. {suma_4}")

# 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
n_5 = 274
mini_5 = 9
while n_5 > 0:
	if n_5 % 10 < mini_5:
		mini_5 = n_5 % 10
	n_5 //= 10
print(f"5. {mini_5}")

### ALGORYTMY ###

a = 13 #int(input("Podaj liczbę: "))

# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza
def CzyPierwsza(a):
	for i in range(2, a // 2 + 1):
		if (a % i == 0):
			return False
		else:
			return True
if CzyPierwsza(a) == True:
	print("1) Liczba jest pierwsza.")
else:
	print("1) Liczba nie jest pierwsza.")

# 2. Sprawdź czy wpisana przez usera liczba jest złożona
if CzyPierwsza(a) == False:
	print("2) Podana liczba jest złożona.")
else:
	print("2) Podana liczba nie jest złożona.")
	
# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
b = 24
while b > 0:
	a, b = b, a % b
if a == 1:
	print("3) Liczba jest względnie pierwsza z 24")
else:
	print("3) Liczba nie jest względnie pierwsza z 24")
	
# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.
klucz = 5
s = input()
szyfr = ""
for i in range(len(s)):
    szyfr = szyfr + chr(65 + (ord(s[i]) - 65 + klucz) % 26)
print(s, szyfr)
	
# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.
a, b, c, d = map(int, input("Podaj: ").split())
def NWW(x, y):
	if x != y:
		nww = x * y
		while y > 0:
			x, y = y, x % y
		nww /= x
		return int(nww)
nww = NWW(b, d) 	
def NWD(d, q):
	while q > 0:
		d, q = q, d % q
	return d

if b != d:
	a_nww = int(a * (nww / b))
	c_nww = int(c * (nww / d))
	suma_a = a_nww + c_nww
	skrot_a = int(suma_a / NWD(suma_a, nww))
	skrot_nww = int(nww / NWD(suma_a, nww))
	if skrot_a == skrot_nww:
		print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {suma_a}/{nww} = {1}")
	elif skrot_a > skrot_nww:
		if skrot_nww == 1:
			print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {suma_a}/{nww} = {skrot_a}/{skrot_nww} = {skrot_a}")
		else:
					print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {skrot_a}/{skrot_nww} = {skrot_a // skrot_nww}  {skrot_a % skrot_nww}/{skrot_nww}")
else:
	suma_a = a + c
	if NWD(suma_a, b) != 1:
		skrot_a = int(suma_a / NWD(suma_a, b))
		skrot_nww = int(nww / NWD(suma_a, b))
		if skrot_a > skrot_nww:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b} = {skrot_a}/{skrot_nww} = {skrot_a // skrot_nww}  {skrot_a % skrot_nww}/{skrot_nww}")
		else:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b} = {skrot_a}/{skrot_nww}")
	else:
		if a > b:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b} = {suma_a // b}  {suma_a % b}/{b}")
		else:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b}")
 # 6. Znajdź NWW dwóch wpisanych przez usera liczb
a, b = map(int, input("Podaj: ").split())

def NWW(a, b):
	iloczyn = a * b
	while b > 0:
		a, b = b, a % b
	nww = int(iloczyn / a)
	return nww
	
print(NWW(a, b))

### KARTKA ###
# 1. Oblicz wartość ONP - 8822+/234*---
# 2. Znajdź postać ONP dla pisanego wyrażenia - (3+8)/4-6*(3*4/2)
# 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb - dowolny i a=35 b=56

### NAPISY ###
# 1. Znajdź ilość liter C we wpisanym napisie
napis_1 = "CYC"
ile_c = 0
for x in napis_1:
	if x == "C":
		ile_c += 1
print(f"C: {ile_c}")

# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
napis_2 = "WODA"
flaga = True
for i in range(1, len(napis_2)):
	if ord(napis_2[i]) > ord(napis_2[i - 1]):
		flaga = False
		break			
if flaga == True: 
	print("Literki w napisie są w porządku nierosnącym")
else:
	print("NIE")
	
# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
dlugosc_wyraz = 0
najw_wyraz = ""
for i in range(3):
	wyraz = input("Podaj: ")
	if len(wyraz) > dlugosc_wyraz:
		dlugosc_wyraz = len(wyraz)
		najw_wyraz = wyraz
print(f"Najdłuższy wyraz to: {najw_wyraz}")

