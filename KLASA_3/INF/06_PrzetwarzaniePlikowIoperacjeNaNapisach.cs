# Zad 1
def Zad_1():
    userFirstname = input("Podaj imię: ")
    userSurname = input("Podaj nazwisko: ")

    DaneOsobowe = open("dane_osobowe.txt", "w")
    DaneOsobowe.write(userFirstname)
    DaneOsobowe.write(userSurname)
    DaneOsobowe.close()

# Zad 2 NIE DOKOŃCZONE
def Zad_2():
    DaneOsobowe = open("dane_osobowe.txt", "r")
    List = DaneOsobowe.readline().rstrip().split()

    for i in range(0, len(list), 2):
        print(f"Witaj {List[i]} {List[i + 1]}")

    DaneOsobowe.close()
