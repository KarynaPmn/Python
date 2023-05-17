napis = input("Podaj napis: ")

# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
print(f"Pierwsza: {napis[0]} i ostatnia: {napis[-1]}")

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
print(napis[1 : -1])

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
print(napis[-1 : -5 : -1])

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisany napis
WagaNapisu = 0
for x in napis:
    WagaNapisu += ord(x)
print(f"Waga napisu: {WagaNapisu}")

# 5. Policz ile we wpisanym napisie jest liter A.
ile_a = 0
for a in napis:
    if a == "A":
        ile_a += 1
print(f"A: {ile_a}")

# 6. Podaj dominującą literkę we wpisanym napisie. Niech to będzie tylko jedna literka.
L = [0] * 100
dominujacaLiterka = 0
maksi = 0
for x in napis:
    L[ord(x)] += 1
for i in range(len(L)):
    if L[i] > maksi:
        dominujacaLiterka = chr(i)
        maksi = L[i]
print(f"Dominująca literka: {dominujacaLiterka}")

# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)
D = [0] * 100
ile_liter = 0
DOMINANTA= []
for x in napis:
    D[ord(x)] += 1
for i in range(len(D)):
    if D[i] == max(D):
        DOMINANTA.append(chr(i))
    if D[i] != 0:
        ile_liter += 1
if len(DOMINANTA) == ile_liter:
    print("Nie ma dominanty.")
else:
    print(f"Dominanta: {DOMINANTA}")

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
ile_la = 0
for i in range(len(napis)):
    if (napis[i] == "L" and napis[i + 1] == "A"):
        ile_la += 1
if ile_la == 3:
    print("TAK.")
elif ile_la == 0:
    print("LA nie występuje w napisie.")
else:
    print(f"LA wustępuje {ile_la} raz.")

### sprawdź czy podany przez usera pociąg jest w napisie ###
pociag = "MMA"
ile_pociag = 0
for i in range(len(napis)):
    flaga = False
    if napis[i] == pociag[0] and i + len(pociag) < len(napis):
        t = i
        for j in range(len(pociag)):
            if napis[t] == pociag[j]:
                flaga = True
            else:
                flaga = False
                break
            t += 1
    if flaga == True:
        ile_pociag += 1
            
if ile_pociag > 0:
    print(f"występuje {ile_pociag} razy.")
else:
    print(f"Nie.")   
    
# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie ułamkowy to zaokrąglij średnią w dół)
from math import floor
srednia = 0
sumaSredniej = 0
for x in napis:
    sumaSredniej += ord(x)
srednia = floor(sumaSredniej / len(napis))
print(f"Średnia: {srednia}")

# 10. Wypisz literki, których nie ma w napisie
N = [0] * 91
brakLiter = ""
for x in napis:
    N[ord(x)] += 1
for i in range(65, 91):
    if N[i] == 0:
        brakLiter += chr(i) + " "
print("Liter brak w napisie: " + brakLiter)

# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)
ilePalindrom = 0
l = 0
while l < len(napis) - 2:
    if (napis[l] == napis[l + 2]):
        ilePalindrom += 1
        print(napis[l : l + 3])
    l += 1
print(f"Palindromy: {ilePalindrom}")
