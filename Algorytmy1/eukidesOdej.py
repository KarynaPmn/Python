# Zad 1 NDW
a, b = int(input()), int(input())

while a != b:
  if a > b: a -= b
  if b > a: b -= a
print(a)