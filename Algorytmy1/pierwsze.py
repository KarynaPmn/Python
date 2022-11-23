# 1. Algorytm sprawdzający czy liczba jest pierwsza
# Do pierwiastka!!!

# #  WERSJA 1
# n = int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza.")
#     exit(0)
# print("Liczba jest pierwsza.")

# # WERSJA 2
# n = int(input())
# flaga = True
# for i in range(2, n):
#   if n % i == 0:
#     flaga = False
# if flaga == True:
#   print("Liczba jest pierwsza.")
# else:
#   print("Liczba nie jest pierwsza.")

#  WERSJA 4
# from math import sqrt
# n = int(input())
# for i in range(2, int(sqrt(n)) + 1):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza.")
#     exit(0)
# print("Liczba jest pierwsza.")

# 2. Generator liczb pierwszych - liczby pierwsze w przedziale [p, q]
# L = "ola ma kota".split("k")
# print(L)
# p, q = map(int, input().split())
# for i in range(p, q + 1):
#   flaga = True
#   for j in range(2, int(i**0.5) + 1):
#     if i % j == 0:
#       flaga = False
#   if flaga:
#     print(i, end=" ")

# Generator liczb pirwszych - początkowe k liczb pierwszych.
n = int(input("Podaj ile chcesz liczb pierwszych:"))
x = 2
while n >=0:
  flaga = True
  for i in range(2, x):
    if x % i == 0:
      flaga = False
  if flaga:
    print(x, end=" ")
    n = n - 1
    if n == 0:
      break
  x = x + 1

  