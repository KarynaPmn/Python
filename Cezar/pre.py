# for i in range(65, 91):
#   print(chr(i), end=" ")

## z napisu literki

# napis = input()

# for i in range(len(napis)):
#   print(napis[i])

## zaszyfruj napis Cezarem w kluczu = 3

# napisz = int(input())
# szyfr = ""

# for i in range(len(napis)):
#   szyfr += chr(ord(napis[i]) + 3)


// 

napis = input()
szyfr = ""
for i in range(len(napis)):
    szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + 3) % 26)
print(napis, szyfr)

