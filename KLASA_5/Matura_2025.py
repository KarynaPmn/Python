# Zad. 1.1

def przestaw_rek(n):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100

    w = 0
    if n > 0:
        w = a + 10*b + 100*przestaw_rek(n)
    else:
        if a > 0:
            w = a + 10*b
        else:
            w = b

    return w

# Zad. 1.3
def przestaw(n):
    wynik = 0
    mnoznik = 1

    while n > 0:
        para = n % 100
        n //= 100

        if para < 10:
            odwrocona = para
        else:
            a = para // 10
            b = para % 10

            odwrocona = b*10 + a

        wynik = wynik + odwrocona*mnoznik
        mnoznik = mnoznik*100

    return wynik

print(przestaw_rek(316245))
print(przestaw(316245))
