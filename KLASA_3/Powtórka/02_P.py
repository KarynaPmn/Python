# Sito Erostenesa
def SieveOfEratosthenes(n):
    listPrimeNumbers = []
    listIfTrue = [True] * (n + 1)
    listIfTrue[0] = False
    listIfTrue[1] = False

    p = 2
    while p * p < n + 1:
        if listIfTrue[p]:
            for i in range(p + p, n + 1, p):
                listIfTrue[i] = False
        p += 1
    
    for number in range(2, n + 1):
        if listIfTrue[number]:
            listPrimeNumbers.append(number)
    
    return listPrimeNumbers

# Zad. 5. --- 
# Napisz program w języku Python, który zapyta użytkownika o podanie dwóch liczb całkowitych a, b, gdzie 2 < a < b, a
# następnie wyświetli wszystkie liczby pierwsze z przedziału [a,b] oraz ich liczbę i sumę, wykorzystując algorytm sita.
# Sito Erostenesa
def SieveOfEratosthenesRange(a, b):
    listPrimeNumbers = []
    listIfTrue = [True] * (b + 1)
    listIfTrue[0] = False
    listIfTrue[1] = False

    p = 2
    while p * p < b + 1:
        if listIfTrue[p]:
            for i in range(p + p, b + 1, p):
                listIfTrue[i] = False
        p += 1
    
    for number in range(a, b + 1):
        if listIfTrue[number]:
            listPrimeNumbers.append(number)
    
    return listPrimeNumbers

def Zadanie_1():
    a, b = map(int, input("Input a range: ").split(" "))

    while not(2 < a and a < b):
        print("Enter incorrect range.")
        a, b = map(int, input("Try again, input range from 2: ").split(" "))
    
    listPrimeNumbers = SieveOfEratosthenesRange(a, b)
    print("\nPrime number:", end=" ")
    for number in listPrimeNumbers:
        print(number, end= " ")
    print("\nQuantity: " + str(len(listPrimeNumbers)))
    print("Sum: " + str(sum(listPrimeNumbers)))

# Wyszukiwanie binarne
def BinarySearch(number, T):
    if IfSorted(T) == False:
        print("List isn't sorted!")
        T = sorted(T)
    
    left = 0
    right = len(T) - 1
    while left < right:
        middle = (right + left) // 2

        if T[middle] < number:
            left = middle + 1
        else:
            right = middle   
    
    return T[left] == number

def IfSorted(T):
    for i in range(len(T) - 1):
        if T[i] > T[i + 1]:
            return False
    return True

def RekuBinarySearch(T, number, left, right):
    if left < right:
        middle = (left + right) // 2
        if T[middle] < number:
            return RekuBinarySearch(T, number, middle + 1, right)
        else:
            return RekuBinarySearch(T, number, left, middle)

    return T[left] == number
    
# Pliki
# Zapisanie danych do pliku
def SafeInfoUser():
    plik = open("dane_osobowe.txt", "w")

    userFirst, userSurname = map(str, input("Name and surname: ").split(" "))
    plik.write(userFirst + "\n")
    plik.write(userSurname + "\n")
    print("Save!")

    plik.close()

# Odczytanie z pliku
def GetInfoUser():
    plik = open("dane_osobowe.txt", "r")
    User = list(map(str, plik.readlines()))

    print(f"Witaj {User[0].rstrip()} {User[1].rstrip()}!")

    plik.close()

# Plik ciagi.txt zawiera w pierwszej linii liczbę ciągów.
# W kolejnych wierszach pierwsza liczba oznacza liczbę wyrazów
# ciągu, a kolejne liczby w wierszu to wyrazy ciągu.
def GetCiag():
    plik = open("ciagi.txt", "r")

    ciagi = int(plik.readline().rstrip())
    print(f"Liczba ciągów: {ciagi}")

    for i in range(ciagi):
        Ciag = plik.readline().rstrip().split()
        print(f"{i + 1} Ma {Ciag[0]} elementów:", end=" ")
        print(Ciag[1:])

    plik.close()

def HowMuchLetters(text):
    Letters = []

    for i in text:
        if i not in Letters:
            Letters.append(i)
    
    print(len(Letters))

# Skleić wyrazy
def JoinWords():
    plik = open("slowa.txt", "r")
    slowa = ''.join(line.strip() for line in plik)
    
    ileA = 0
    for l in slowa:
        if l == "A": 
            ileA += 1

    print(ileA)
