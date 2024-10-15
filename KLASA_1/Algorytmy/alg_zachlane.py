T = [50, 20, 10, 5, 2, 1]
x = int(input())
ilosc = 0

# SPOSÓB 1
for i in T:
	ilosc = x // i
	x = x - ilosc * i
	print(f"Nominał {i} ilość {ilosc}")

print()
print()

# SPOSÓB 2 
for i in T:
	ilosc = x // i
	if i > 0:
		x = x - ilosc * i
		print(f"Nominał {i} ilość {ilosc}")
