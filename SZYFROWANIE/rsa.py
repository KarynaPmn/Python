# PRE
# funkcja licząca NWD
# from math import gcd 
# print(gcd(12,16))

# 1.Wybór 2 dużych liczb pierwszych
p = 11
q = 13
print(p,q)
# 2.Stworzenie funkcji Eulera F= (p-1) * (q-1) i znalezienie n = p*q
F= (p-1) * (q-1)
n = p*q
print(n)
print(F)
# 3.Znalezienie klucza publicznego e: NWD(F,e) = 1
from math import gcd 
for i in range(2,F):
  if gcd(i,F) == 1:
    e = i 
    break
print(e,n)
# 4.Wygenerowanie klucza prywatnego d: d*e mod F = 1 (odwrotność modulo)
for i in range(2,n):
  if (i*e) % F == 1:
    d=i
    break
print(d,n)
# 5.Przykład działania
# c = x**e mod n (szyfrogram)
# t = c**d mod n (na tekst jawny)
msg = input()
szyfrogram = ""
for i in msg:
  szyfrogram += chr(ord(i)**e % n)
print(szyfrogram)

jawny=""
for j in szyfrogram:
  jawny += chr((ord(j)**d) % n)
print(jawny)
