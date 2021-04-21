from random import randint

los = randint(1, 10)
odp = -1
i = 0
print("Zgadnij liczbę 1-10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Wybrałeś większą liczbę, spróbuj ponownie.")
    elif odp < los:
        print("Wybrałeś mniejszą liczbę, spróbuj ponownie.")
print("Brawo! Odgadłeś za", i, "razem! Wylosowana liczba to:", los,)


