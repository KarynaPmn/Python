# Sprawdź czy wpisana przez usera liczba jest parzyst

a = input()
def CzyParzystaBin(a):
    if (a[-1] == "0"):
        #print("Liczba jest parzysta.")
        return True
    else:
        #print("Liczba jest nie parzysta.")
        return False

# Określ parzystość sumy/różnicy/iloczynu dwóch wpisanych przez usera liczb binarnych

def  SumaRoznicaIloczynBin():
    a1 = input()
    b1 = input()

    if (CzyParzystaBin(a1) == CzyParzystaBin(b1)):
        print("Suma jest parzysta")
    else:
        print("Suma jest nie parzysta")

# 1. Napisz alg dodawania dwóch liczb binarnych o tej samej długości.
def DodawanieBin():
    x, y = input(), input()
    w = ""
    j = 0

    for i in range(len(x) - 1, -1, -1):
        s = int(x[i]) + int(y[i])
        j = s // 2
        w = str(s % 2) + w
    print(w) 

    if j > 0:
        w = str(j) + w
DodawanieBin()
        
# 2. Napisz algorytm dodawania dwóch liczb binarnych o różnej długości.

# 3. Wypisz wszystkie liczby binarne sześciocyfrowe, w których liczba jedynek jest 2 razy większa od liczby zer.






