# print("Zadanie 2")
# n = int(input("Liczba:"))
# for i in range(1, n+1):
#   print("*", end=" ")
#   if i % 2 == 1:
#     print("|"*i, end="")
#   else:
#     print("-"*i, end="")

# # PRE - TabMn
# for i in range(1,11):
#   for j in range(1,11):
#     print(i*j, end="\t")
#   print()

# # PRE na 2 pętle
# n = int(input("Liczba:"))
# for i in range(n): 
#   for j in range(n+i): 
#     print("*", end="")
#   print()

#   for k in range(n):
#     for l in range(n-i): 
#       print("*", end="")
#     print()

# print("Zadanie 3")
# n = int(input("Podaj liczbę:"))
# for i in range(1,n):
#   print("*")
#   if n % 2 == 1:
#     print("|" * i)
#   elif n % 2 == 0:
#     print("-" * i)
# n = int(input())
# for i in range(n):
#   for j in range(n-i-1):
#     print(" ", end="")
#   for k in range(n-i-1, n):
#     print("*", end="")
#     print()
# print()
# for i in range(n):
#   for j in range(n):
#     if i >= j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()
# print()
# for i in range(n):
#   for j in range(n):
#     if i <= n - j - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()
# print()
# for i in range(n):
#   for j in range(n):
#     if j >= i:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()
# print()

# for i in range(n):
#   for j in range(n):
#     if j >= i - j - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()
    #Zad 5
n = int(input()) 
# for i in range(n):
#   for j in range(n):
#     if j == n // 2:
#       print("*", end="")
#     elif i == n // 2:
#       print("-",end="")
#     else:
#       print(" ",end="")
#   print() 

# Zad 6
for i in range(n):
  for j in range(n):
    if i - j == 0:
      print("*", end="")
    elif(j + i == n - 1):
      print("?", end="")
    else:
      print(" ", end="")
  print()
      
  
  
    
    
    


