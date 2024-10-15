# ZADANIE 1 -- Oblicz ile ma bloków.
def HowManyBlocks(n):
    #n = input("Podaj binarkę: ")
    howManyBlocks = 1
    homManyElementsInBlock = 1

    for i in range(1, len(n)):
        if (n[i] == n[i - 1]):
            homManyElementsInBlock += 1
        else:
            homManyElementsInBlock = 1
            howManyBlocks += 1
    
    #print(f"Dana binarka ma {howManyBlocks} bloków.")
    return howManyBlocks

# ZADANIE 2 -- Ile liczb w pliku składa się z co najmniej z dwóch bloków.
def Zadanie_2():
    # Tryby open --> with open('binaria_liczby.txt', 'r') as plik::
    ### 'r' --> odczyt (read)
    ### 'r+' --> czytanie i zapis
    ### 'w' --> zapis
    ### 'a' --> dopisywanie
    ### itp.

    # with --> zapełnia, że po zakończeniu jego wykonania plik zostanie automatycznie zamknięty 

    with open('binaria_liczby.txt') as file:
        FileContents = file.read().split()

    HowManyNumbers = 0
    for element in FileContents:
        if (HowManyBlocks(element) >= 2):
            print(element)
            HowManyNumbers += 1
    print(f"W pliku znajduje się {HowManyNumbers} z co najwyżej dwóch bloków.")

# ZADANIE 3 -- Wypisz największą z liczb w pliku, nie konwertując na dziesiętne.
def Zadanie_3():
    with open('binaria_liczby.txt') as file:
        FileContnts = file.read().split()
    
    maxBin = 0
    for element in FileContnts:
        binTodec = 0
        for i in range(len(element) - 1, -1, -1):
            if (element[i] == '1'):
                binTodec += pow(2, (len(element) - 1 - i))

        if (binTodec > maxBin):
            maxBin = binTodec
    
    print(f"Największą licbą z binarii jest {maxBin}")

# ZADANIE 4 -- Czy jest palindromem.
def Zadanie_4():
    binar = '111010101'
    ifPolindrom = True

    # SPOSÓB I
    for i in range(len(binar) // 2):
        if (binar[i] != binar[len(binar) - i - 1]):
            ifPolindrom = False
            break
    
    if (ifPolindrom):
        print("Tak to jest polindrom!")
    else:
        print("To nie jest żaden polindrom!")
        ifPolindromNewChance = True
        for i in range(1, len(binar) // 2):
            if (binar[i] != binar[len(binar) - i]):
                ifPolindromNewChance = False
                break

        if (ifPolindromNewChance):
            print("Jednak masz szans jeżeli dadam jeden bit ;)")
        else:
            print("Nie masz szans to naprawić już :[")
    print()

    ############
    # SPOSÓB II
    bin = "".join(reversed(binar))
    print(bin)

    if (binar == bin):
        print("Tak to jest polindrom")
    else:
        print("To nie jest polindrom")
        if (binar[1::] == bin[:-1:]):
            print("Jednak może być polindromem po dodaju jednogo bitu.")
        else:
            print("Nawet po dodaniu jednego bitu nie stanie się polindromem.")

# ZADANIE 5 -- Mnożennie binarne (5-cyfrowe i 3-cyfrowe)
def Zadanie_5():
    a = "10101"
    b = "101"
    Suma = []

    for i in range(len(b) - 1, -1, -1):
        if (b[i] == "0"):
            Suma.append("00000")
        else:
            Suma.append(a)
    
    Suma[0] = "00" + Suma[0]
    Suma[1] = "0" + Suma[1] + "0"
    Suma[2] = Suma[2] + "00"

    for i in range(len(Suma)):
        print(Suma[i])
    
    W = "0000000"

    for i in range(len(W)):
        W = W[:i] + str(int(W[i]) + int(Suma[0][i]) + int(Suma[1][i]) + int(Suma[2][i])) + W[i + 1:]
    W = "0" + W

    Wynik = list(W)
    for i in range(len(Wynik) - 1, 0, -1):
        Wynik[i - 1] = str(int(Wynik[i]) // 2 + int(Wynik[i - 1])) 
        Wynik[i] = str(int(Wynik[i]) % 2)

    if (Wynik[0] == "0"):
        print("".join(Wynik[1::]))
    else:
        print("".join(Wynik)) 
