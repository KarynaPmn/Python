import random
T = []

for i in range(40):
    T.append(random.randint(10, 99))
print(T)

C = []
ile = 1

for i in range(len(T) - 1):
	if T[i] < T[i + 1]:
		ile += 1
	else:
		C.append(ile)
		ile = 1
print(C)

print(f"MAks: {max(C)}")