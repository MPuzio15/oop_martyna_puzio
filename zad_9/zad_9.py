'''
Zadanie 9:  [KOD] Do czego służy słowo kluczowe super.
Napisz przykład jego użycia (2 pkt).

Slowa kluczowego super() używamy do wywolania w konstruktorze klasy
pochodnej metody __init__ z klasy bazowej.
Wskazujemy w ten sposób, które pola mają być odziedziczone, a dodatkowo możemy
zadeklarować dodatkowe pola w danym konstruktorze, które nie beda dostepne np wklasie bazowej,
ale juz w klasie pochodnej danej klasy bedziemy mieli do nich dostep przy uzyciu super(), np:
'''


class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def print_out_details(self):
        print(f'I am {self.name} and I am {self.age}')


class Employee(Person):
    def __init__(self, name, lastname, age, id):
        super().__init__(name, lastname, age)
        self.id = id

    def print_out_details(self):
        print(f'I am {self.name} and I am {self.age}. My Id is{self.id}')


class HrEmployee(Employee):
    def __init__(self, name, lastname, age, id, number_of_interviews_arranged):
        super().__init__(name, lastname, age, id)
        self.number_of_interviews_arranged = number_of_interviews_arranged

    def print_out_details(self):
        print(
            f'I am {self.name} and I am {self.age}.\nMy id is {self.id}. I have arranged {self.number_of_interviews_arranged}')


osoba = Person("Jan", "Kowalski", 50)
pracownik = Employee("Adam", "Kot", 15, 123456)
hrowiec = HrEmployee("Piotr", "Lis", 34, 34256354, 12)
osoba.print_out_details()
pracownik.print_out_details()
hrowiec.print_out_details()
