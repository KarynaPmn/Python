# kod hufmana

W = "ABCCCDDDDDEFGGGHHIJJ"
E = "AB3C5DEF3G2HI2J"

H = ""
ilosc = 1 
for i in range(len(W)-1):
  if W[i] == W[i+1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
    ilosc = 1
if ilosc > 1:
  H += str(ilosc)
H += W[len(W)-1]
print(W)
print(H)
