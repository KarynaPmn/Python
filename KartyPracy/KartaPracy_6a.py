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

print("Zadanie 5")

a = int(input())

for b in range(10, 19):
    x = a
    y = b
    while y > 0:
        x, y = y, x % y
    if x == 1:
        print(f"Liczba {b} jest względnie pierwsza do liczby {a}.")

print("Zadanie 6")

a, b = int(input()), int(input())
x = a
y = b

while y > 0:
    x, y = y, x % y

i = a // x
m = b // x

if m == 1:
    print(f"{a}/{b} = {i}")
else:
    if a == i:
        print(f"{a}/{b} nie da się skrócić.")
    else:
        print(f"{a}/{b} = {i}/{m}")
        
print("Zadanie 7")

a, b = int(input()), int(input())
m = a
s = 0

if a > b:
    m = a % b
    s += a // b
    if m == 0:
        print(f"{a}/{b} = {s}")
    else:
        print(f"{a}/{b} = {s} {m}/{b}")
elif a == b:
        print(f"{a}/{b} = 1")
else:
    print(f"{a}/{b} nie da się skrócić.")
    
 print("Zadanie 9")

n = int(input("Podaj ile chcesz liczb prewiepierwszych: "))
flaga = True

x = 2
while 1:
    flaga = True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            flaga = False
    if flaga:
        print(x * 2, end=" " )
        n = n - 1
        if n == 0:
            break
    x = x + 1
