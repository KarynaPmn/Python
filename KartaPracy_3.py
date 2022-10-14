# pętla liczb dwucyfrowych nieparzystych od 15 do 31
#for i in range(15,33,2): print(i)
# pętla liczb dwucyfrowych malejąco (step ujemny)
#for i in range(99, 9, -1): print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step dodatni)
#for i in range(10, 100, 1): print(109 - i, end=" ")
# pętla liczb trzycyfrowych podzielnych przez 20
# for i in range(100, 1000, 20): print(i, end=" ")
# for i in range(5, 50, 1): print(i*20, end=" ")

# Zad 1
# n=int(input())
# for i in range(n):
#     print(1**3 + 3, end=" ")
#
# # Zad 2
# for i in range(105, 1000, 15):
# pr
#
# # zad 3
# n = int(input())
# for i in range(1, n+1):
# if n % 1 == 0:
# print(i, end=" ")
#
# # Zad 4
# suma = 0
# for i in range(10,100):
# suma = suma + 1
# print(suma)

# # Zad 5
# n = int(input())

# suma = n*(n+1)//2

# for i in range(n-1):
#   x = int(input())
#   suma = suma - x
# print("Nie podałeś:", suma)

# Zad 6
n = int(input())
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(n-2):
  a, b = b, a + b
  print(b, end=" ")