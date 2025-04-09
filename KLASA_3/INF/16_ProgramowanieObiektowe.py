### Przykład 1. ###
class Prostokat:
    def __init__(self, dlugosc, szerokosc):
        self.a = dlugosc
        self.b = szerokosc

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return self.a * 2 + self.b * 2

def Zad_2():
    prostokat = Prostokat(3, 5)
  
    print("Pole prostakąta o bokach: ", prostokat.a, " i ", prostokat.b, "wynosi: ", prostokat.pole())
    print("Obwód prostakąta o bokach: ", prostokat.a, " i ", prostokat.b, "wynosi: ", prostokat.obwod())

### Przykład 2. ###
class ProstokatExtra(Prostokat):
    def __init__(self, x, y):
        super().__init__(x, y)

    def wyswietlPole(self):
        print("Pole prostakąta o bokach: ", self.a, " i ", self.b, "wynosi: ", self.pole())

def Zad_3():
    prostokat = ProstokatExtra(3, 5)
    prostokat.wyswietlPole()

### Przykład 3. ###
class Prostokad_3:
    a = 0
    b = 0

    def pole(self):
        return self.a * self.b

def Zad_3():
    prostokat = Prostokad_3()
    prostokat.a = int(input("Podaj a: "))
    prostokat.b = int(input("Podaj b: "))

    print("Pole prostokąta wynosi:", prostokat.pole())
