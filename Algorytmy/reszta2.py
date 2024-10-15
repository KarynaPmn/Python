T = [50, 20, 10, 5, 2, 1]
x = int(input())
ilosc = 0
W = []

for i in T:
	ilosc = x // i
	if i > 0:
		x = x - ilosc * i
		for j in range(ilosc):
			W.append(i)
print(W)

# opcjonalnie zamiast appenda w forze: W = W + ilosc*[i]
# for i in T:
# 	ilosc = x // i
# 	if i > 0:
# 		x = x - ilosc * i
# 		W = W + ilosc*[i]
# print(W)