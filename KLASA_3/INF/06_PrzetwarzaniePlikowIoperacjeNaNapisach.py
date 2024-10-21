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
    print(f"Średnia: {statistics.mean(LosoweLiczby)}") # statistics.mean() --> oblicza średnią liczb z listy

