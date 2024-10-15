# Zamiana na binarne
liczba = 39

def dec2bin(n):
    x = n
    wynik = ''
    while x > 0:
        wynik = str(x % 2) + wynik
        x //= 2
    return wynik
print(dec2bin(liczba))
    

# Rekurencyjnie I
def dec2binreku(n):
    wynik1 = ''
    if n == 0:
        return ""
    return dec2binreku(n // 2) + str(n % 2)
print(dec2binreku(liczba))


# Rekurencyjnie II
def dec2binreku2(n):
    if n == 0:
         return
    dec2binreku2(n // 2)
    print (n % 2, end = "")
dec2binreku2(liczba)

# Zamiana na binarny

def bin2dec(n):
    s = 0
    for i in range(len(n)):
        s = s + 2**i * int(n[-i-1])
    return s
print()
print(bin2dec("10011"))

# Sposób Hornera - nie obowiązkowe
def bin2decHorner(n):
    w = 0
    for i in range(len(n)):
        w = w * 2 + int(n[i])
    return w
print(bin2decHorner("10011"))

# Rekurencyjnie

