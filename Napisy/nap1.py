# s = input()
# # napis (string) to jakby "lista", więc działa foreach i for z range
# for x in s:
# 	print(x)

# for i in range(len(s)):
# 	print(s[i])

# # napis to nie jest lista sensu stricte
# L = [7, 2, 8, 5, 3]
# L.sort()
# #  s.sort() - to byłby błąd! Napis to nie jest "pełna" lista
# print(s, L)

# # Zmiana napisu na listę
# S = list(s)
# print(S)
# S.sort()
# print(S)
# # join - robi z listy string
# w = "-".join(S)	# s-t-r-i-n-g
# print(w) 

# sprawź czy wpisane słowo jest palindromen

r = input()
R = list(r) 
L = R.copy()
R.reverse() # [g, n, i, r, t, s]
print(L, R)
if L == R:
	print("Jest palindronem.") #oko
else:
	print("Nie jest palindronem.") 