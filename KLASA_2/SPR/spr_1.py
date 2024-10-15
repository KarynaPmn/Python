import math

def f(x):
    return -x**3 + 2 * (x**3) + x

def g(x):
    return -x**3 + 2 * (x**3) + x + 1

def Trapez(a, b, n, myFuction):
    dx = (b - a) / n
    suma = 0
    for i in range(n):
        suma += ((myFuction(a + dx * i) + myFuction(a + dx * i + dx)) * dx) / 2
    return suma

# Ile worków nawozu trzeba kupić by to nawiźć nawozem do traw firmy "Nawóz do traw"?
# 1 worek --> 5 kg ziemi
# 1 kg ziemi --> 5 m^2
# 1 km^2 --> 1 000 000 m^2
# n = dzień urodzenia + 15

def IleWorkow(powierzchnia_dzialki):
    powierzchnia_dzialki *= 1000000 # km^2 -> m^2
    ile_kg = powierzchnia_dzialki / 5
    ile_workow = math.ceil(ile_kg / 5)

    return ile_workow

# Dane
a = 0
b = 2
n = 19
powierzchnia_d = Trapez(a, b, n, f)
powierzchnia_g = Trapez(a, b, n, g)

print(f"Powierzchnia dolnej części wynosi: {powierzchnia_d}.")
print(f"Powierzchnia górnej części wynosi: {powierzchnia_g}.")
print(f"Powierzchnia działki pod rzeką wynosi: {powierzchnia_d}.")
print(f"Dla uzupełniania działki potrzebujesz zakupić {IleWorkow(powierzchnia_d) + IleWorkow(powierzchnia_g)} worków.")



