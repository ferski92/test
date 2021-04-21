wiek = 13
kasa = 25

if wiek >=18:
    if kasa >= 35:
        print("Wejscie")

print("inna opcja")

if wiek >=18 and kasa >=35:
    print("Wbijaj")

if wiek <= 12 or kasa >=30:
    print("moze wejsc")
else:
    print("sory nie wbijesz")

if not wiek > 12 or kasa >= 30:
    print('dawaj dawaj gnoju')
else:
    print('nie wjedziesz gnojku')

#kolejosc ma znaczenie
if (True or False) and not False:
    print("prawda")
else:
    print("falsz")