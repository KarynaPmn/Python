def potega(a, n):
    w = 1

    while n > 0:
        w *= a

        a *= a
        n //= 2
    
    return w

print(potega(4, 4))
