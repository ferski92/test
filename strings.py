napis1="Champion"
napis2="babeczki truskawkowe"
print(len(napis1))
print(len(napis2))
print(len(napis1 + napis2))
print(len(napis1) + len(napis2))
txt="hello"
print(txt[0])
t = txt[2]+txt[3]
print(t)
txt = txt[0] + 'a' + txt[2:]
print(txt)

print(napis2[1:10])
print(napis1.lower())
print(napis1.upper())
print(napis1.swapcase())
print(napis1.title())
print("-".join(napis1))
print(napis1.strip("C"))
print(min("lolbz"))
print("ala ma kota".strip("a "))
print("Python Jest Fajny".istitle()) #zwraca true jesli kazdy wyraz zaczyna sie z duzej litery
print()
""" ZADANIA """
sentence = "Kurs Pythona jest prosty i przyjemny."
print(len(sentence))
print(sentence[18:24])
print(sentence[7])
print(sentence[-4])
print(sentence[0] + 'o' + sentence[2:])
sentence = sentence[20] + 'z' + sentence[22:]
print(sentence)

"""ZADANIE 2"""

q1 = input("Podaj imię: ")
q2 = input("Podaj nazwisko: ")
q3 = input("Podaj numer telefonu: ")
print(q1.isalpha())
print(q2.isalpha())
print(q3.isdigit())
print(q1.title())
print(q2.title())
print(q3.replace(" ",""))
