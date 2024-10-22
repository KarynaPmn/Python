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
    plik = open("slowa.txt", "r")
    Slowa = plik.readlines()

    print("1. wyświetli ponumerowane słowa z pliku tekstowego")
    print("2. wyświetli liczbę słów w pliku")
    print("3. wyświetli słowa zaczynające się na literę A")
    print("4. wyświetli słowa kończące się na literę A")
    print("5. wyświetli słowa oraz liczbę liter, z których się składają")
    print("6. *wyświetli najkrótsze oraz najdłuższe słowo w pliku oraz ich długość (jeżeli jest ich kilka wyświetl pierwsze z nich)")
    print("7. wyświetli słowa o długości 6")
    print("8. wyświetli słowa zawierające literę O oraz dla każdego z tych słów liczbę tych liter O")
    print("9. wyświetli ile razy w całym pliku występuje litera A")
    number = input("Podaj wybór: ")

    plik.close()
