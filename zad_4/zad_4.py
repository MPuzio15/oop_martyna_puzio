'''Zadanie 4 [KOD]: W jednej linijce wygeneruj listę
sześcianów liczb od 1 do 10 (włącznie) i
przypisz ją do zmiennej szesciany. (3 pkt.) '''

szesciany = [x**3 for x in range(11)]
print(szesciany)