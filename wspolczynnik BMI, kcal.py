#print('Oblicz współczynnik BMI')
#waga = input('Podaj swoją wagę: ')
#wzrost = input("Podaj swój wzrost: ")
#print("BMI=Waga/Wzrost^2")
#BMI = int(waga) / float(wzrost)**2
#print("Twój współczynnik BMI wynosi:", BMI)
#print("Twoje BMI wynosi:",int(waga)/float(wzrost)**2)
#del waga
#del wzrost
print("\n")
print('Zapotrzebowanie kaloryczne')
waga = input("Podaj wagę:")
wzrost = input("Podaj wzrost:")
wiek = input("Podaj wiek:")
#S = int(input("M/K?:"))
#M = + 5
S = - 161
PPM = 10*int(waga) + 6.25 * float(wzrost) - 5 * int(wiek) + S
print("Twoje podstawowe zapotrzebowaie kaloryczne wynosi:", PPM)
#akt = input("Wybierz swoją aktywność (a1-a5):")
a1 = 1.2
a2 = 1.4
a3 = 1.6
a4 = 1.8
a5 = 2.0

print("Twoje ogolne zapotrzebowanie wynosi:", PPM * 1.6)

