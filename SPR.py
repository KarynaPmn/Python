import random
T = []

for i in range(40):
    T.append(random.randint(10, 99))
print(T)
print()

C = []
I = []
ile = 1

for i in range(len(T) - 1):
	if T[i] < T[i + 1]:
		ile += 1
	else:
		C.append(ile)
		ile = 1
		
print(C)
print(C.index(max(C)))

for i in range(len(C)):
	if C[i] == max(C):
		I.append(i)
print(f"Maks: {max(C)}, pozycja: {I}")