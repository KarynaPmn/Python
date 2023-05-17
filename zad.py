a, b, c, d = map(int, input("Podaj: ").split())
def NWW(x, y):
	if x != y:
		nww = x * y
		while y > 0:
			x, y = y, x % y
		nww /= x
		return int(nww)
nww = NWW(b, d) 	
def NWD(d, q):
	while q > 0:
		d, q = q, d % q
	return d

a_nww = int(a * (nww / b))
c_nww = int(c * (nww / d))
suma_a = a_nww + c_nww
k = suma_a // nww
l = suma_a % nww
if suma_a < nww:
	print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {suma_a}/{nww}")
else:
	print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {suma_a}/{nww} = {k} {l}/{nww}")

######
a, b, c, d = map(int, input("Podaj: ").split())
def NWW(x, y):
	if x != y:
		nww = x * y
		while y > 0:
			x, y = y, x % y
		nww /= x
		return int(nww)
nww = NWW(b, d) 	
def NWD(d, q):
	while q > 0:
		d, q = q, d % q
	return d

if b != d:
	a_nww = int(a * (nww / b))
	c_nww = int(c * (nww / d))
	suma_a = a_nww + c_nww
	skrot_a = int(suma_a / NWD(suma_a, nww))
	skrot_nww = int(nww / NWD(suma_a, nww))
	if skrot_a == skrot_nww:
		print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {suma_a}/{nww} = {1}")
	elif skrot_a > skrot_nww:
		if skrot_nww == 1:
			print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {suma_a}/{nww} = {skrot_a}/{skrot_nww} = {skrot_a}")
		else:
					print(f"{a}/{b} + {c}/{d} = {a_nww}/{nww} + {c_nww}/{nww} = {skrot_a}/{skrot_nww} = {skrot_a // skrot_nww}  {skrot_a % skrot_nww}/{nww}")
else:
	suma_a = a + c
	if NWD(suma_a, b) != 1:
		skrot_a = int(suma_a / NWD(suma_a, b))
		skrot_nww = int(nww / NWD(suma_a, b))
		if skrot_a > skrot_nww:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b} = {skrot_a}/{skrot_nww} = {skrot_a // skrot_nww}  {skrot_a % skrot_nww}/{skrot_nww}")
		else:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b} = {skrot_a}/{skrot_nww}")
	else:
		if a > b:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b} = {suma_a // b}  {suma_a % b}/{b}")
		else:
			print(f"{a}/{b} + {c}/{d} = {suma_a}/{b}")
	