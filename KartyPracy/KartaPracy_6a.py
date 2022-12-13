print("Zadanie 1")
x = int(input())
suma = 0
while x > 0:
  suma += x % 10
  x = x // 10
print(suma)

print("Zadanie 2")
n = int(input())
flaga = True
for i in range(2, n):
  if n % i == 0:
    flaga = False
if flaga or n != 1:
  print("Liczba jest piewsza.")
else:
  print("Liczba nie jest pierwszą.")

print("Zadanie 3")
n = int(input())
suma = 0

for i in range(1,n)
  if n % i == 0:
    suma += i
if suma == n:
  print("Liczba jest doskonała.")
else:
  print("Liczba nie jest doskonała.")

print("Zadanie 4")
x, y = int(input()), int(input())

while y > 0:
    x, y = y, x % y
if x == 1:
    print("Liczby są względem siebie pierwsze.")
else:
    print("Liczby nie są względem siebie pierwsze.")


