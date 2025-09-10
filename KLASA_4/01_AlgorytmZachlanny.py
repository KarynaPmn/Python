plik = open("nominaly.txt", "r")
nominaly = list(map(int, plik.readline().split()))
plik.close()

def Zad_1(kwota):
   for nominal in nominaly:
       ile = 0
       ile = kwota // nominal
       kwota = kwota % nominal

       if (ile > 0):
           print(nominal, " x ", ile)

def Zad_4():
    N = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    l = int(input("Podaj liczbę: "))
    
    for nominal in N:
        ile = 0
        ile = l // nominal
        l = l % nominal
        
        # Dokończyć zadanie         
