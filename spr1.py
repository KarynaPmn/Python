def sumaCyfr(a):
	licznik = 0
	while a > 0:
		licznik += a % 10
		a //= 10
	return licznik


def NWD(a, b):
	while a != b:
		if a > b: a -= b
		if b > a: b -= a
	return a

l = 0 

for i in range(10, 100):
	if i % sumaCyfr(i) == 0 and NWD(i, sumaCyfr(i)) == sumaCyfr(i):
		l = i // NWD(i, sumaCyfr(i))
		mianownik = sumaCyfr(i) // NWD(i, sumaCyfr(i))
		print(f"{sumaCyfr(i)}/{i} = {mianownik} / {l}")
