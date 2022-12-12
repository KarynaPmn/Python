# for i in range(65, 91):
#   print(chr(i), end=" ")

## z napisu literki

# napis = input()

# for i in range(len(napis)):
#   print(napis[i])

## zaszyfruj napis Cezarem w kluczu = 3

# napisz = int(input())
# szyfr = ""

# for i in range(len(napis)):
#   szyfr += chr(ord(napis[i]) + 3)

# Zad 1 
a, b, c = int(input()),int(input()), int(input())
iloczyn = a * b

while b != a:
  if a > b: a -= b
  if b > a: b -= a

print(iloczyn // a)

