""" ZADANIE:
    * SPIS OGLADANYCH SERIALI VOL 2

    ^^^^^^^^^^^^^^^^^^^^ PS
"""

serial = {'Better' : 10, 'Kosmos' : 7, 'WTF': 2}
print(list(serial.keys()))
#serial.values('Better')

ask1 = input("What serial do you want to watch?: ")

if ask1 == "Better" :
    print("For me...  the ' Better' is " + serial("Better") + "in my rate!")
elif ask1 == "Kosmos":
    print("For me...  the ' " + serial.keys(1) + "' has " + serial.values(1) + "in my rate!")
else:
    print("For me...  the ' " + serial.keys(2) + "' has " + serial.values(2) + "in my rate!")