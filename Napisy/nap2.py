# # ANAGRAM przez sortowanie
# a, b = input(), input()
# X, Y = list(a), list(b)
# X.sort()
# Y.sort()
# a, s = "".join(X), "".join(Y)
# print(a, b)
# if a == b:
# 	print("TAK.")
# else: print("NIE.")

# ANAGRAM przez tablicę
a, b = input(), input()
X, Y = [0] * 150, [0] * 150
print(X)
for i in range(len(a)):
	X[ord(a[i])] += 1
for i in range(len(b)):
	X[ord(b[i])] += 1
if X == Y: 	print("TAK.")
else: 			print("NIE.")

# ONP - odwrotne notowanie pd.