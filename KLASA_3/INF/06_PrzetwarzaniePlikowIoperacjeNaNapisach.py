import random
import statistics


# Zad 1
def Zad_1():
    userFirstname = input("Podaj imię: ")
    userSurname = input("Podaj nazwisko: ")

    DaneOsobowe = open("dane_osobowe.txt", "a")
    DaneOsobowe.write(userFirstname + "\n")
    DaneOsobowe.write(userSurname + "\n")

    print("Zapisane!")
    DaneOsobowe.close()

# Zad 2
def Zad_2():
    plik = open("dane_osobowe.txt", "r")
    DaneOsobowe = plik.readlines()

    for i in range(0, len(DaneOsobowe), 2):
        imie = DaneOsobowe[i].strip()
        nazwisko = DaneOsobowe[i + 1].strip()

        print(f"Witaj {imie} {nazwisko}")

    plik.close()

# Zad 3
def LosoweLiczbyDoPliku(path):
    plik = open(path, "w")

    for i in range(10):
        plik.write(str(random.randint(1, 100)) + "\n")

    plik.close()

def SumaLiczb(list):
    suma = 0

    for i in list:
        suma += i

    return suma

def Zad_3():
    path = "losowe.txt"
    LosoweLiczbyDoPliku(path)
    plik = open(path, "r")
    LosoweLiczby = list(map(int, plik.readlines()))

    print(LosoweLiczby)

    print(f"Suma liczb: {SumaLiczb(LosoweLiczby)}")
    print(f"Max: {max(LosoweLiczby)}")
    print(f"Min: {min(LosoweLiczby)}")
    print(f"Średnia: {statistics.mean(LosoweLiczby)}")  # statistics.mean() --> oblicza średnią liczb z listy

# Zad 4
def Zad_4():
    plik = open("ciagi.txt", "r")

    ileCiag = 0
    for ciag in plik:
        suma = len(ciag.split())

        if suma % 2 == 0:
            ileCiag += 1

    print(f"W ciągu jest: {ileCiag}")
    plik.close()

# Zad 5 -- Nie zakończone !!!
def Zad_5():
    def IleLiter(text): # Dopisać!
        
    plik = open("slowa.txt", "r")
    Slowa = list(map(str, plik.readlines()))

    print("1. Wyświetl ponumerowane słowa z pliku tekstowego")
    print("2. Wyświetl liczbę słów w pliku")
    print("3. Wyświetl słowa zaczynające się na literę A")
    print("4. Wyświetl słowa kończące się na literę A")
    print("5. wyświetl słowa oraz liczbę liter, z których się składają")
    print("6. *wyświetl najkrótsze oraz najdłuższe słowo w pliku oraz ich długość (jeżeli jest ich kilka wyświetl pierwsze z nich)")
    print("7. wyświetl słowa o długości 6")
    print("8. wyświetl słowa zawierające literę O oraz dla każdego z tych słów liczbę tych liter O")
    print("9. wyświetl ile razy w całym pliku występuje litera A")
    number = input("Podaj wybór: ")

    if number == 1:
        for i in range(len(Slowa)):
            print(f"{i + 1}.) {Slowa[i]}")
    elif number == 2:
        print(len(Slowa))
    elif number == 3:
        for word in Slowa:
            if word[1] == "a":
                print(word, end=" ")
    elif number == 4:
        for word in Slowa:
            if word[-1] == "a":
                print(word, end=" ")
    elif number == 5: # Nie zakończone
        for i in range(len(Slowa)):
            print(f"{i + 1}.) {Slowa[i]} -- {IleLiter(Slowa[i)}")


    plik.close()

Zad_5()
