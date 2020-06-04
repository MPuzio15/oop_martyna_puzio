'''
Zadanie 5: W poniższym kodzie wskaż dopisując komentarz wszystkie: (5 pkt.)
Pola (atrybuty) klasy Tamagotchi
Metody klasy Tamagotchi
Argumenty metod klasy Tamagotchi
Wszystkie instancje klasy Tamagotchi
Konstruktor
Klasę bazową
Klasę pochodną
'''


# Klasa bazowa
class Empty:
    pass


# klasa pochodna
class Tamagotchi(Empty):
    # Pola (atrybuty) klasy Tamagotchi
    prog_nudy = 5
    prog_glodu = 10

    # Metody klasy Tamagotchi
    # Konstruktor - metoda __init__
    def __init__(self, imie):
        self.imie = imie
        self.slowa = ["Mmmmrrp", "Hrrp"]
        self.poziom_nudy = 0


# Argumenty metod klasy Tamagotchi - przy wywolaniu czyli w tym przypadku "Burek"
# Wszystkie instancje klasy Tamagotchi - burek
burek = Tamagotchi("Burek")
