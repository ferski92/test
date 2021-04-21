quote="""To jest wielolinijkowy tekst
zawierający cytat
"Always code as if the guy who ends up maintaining your code will be a
violent psychopath who knows where you live"
-John Wood"""
print(quote)
print()
print('czeko', end='')
print('lada', end='\n')
print()

list = [1, 2, 3, "a", "b",]
print(list)
print(list + ["c", "d"]) #listy mozna dodawac i mnozyć
print(list * 2)
print("Ilość elementów: ", len(list))
list.append(["c", "d"]) #przypisanie na stale kolejnej wartosci
print(list)
print(list[0]) #odwolanie sie do 1 elementu listy
print(list[5][1]) #odwolanie sie do 1 elementu z listy w liscie
list.insert(3, 3) #dorzucenie za 3 indexem kolejnej 3
print(list)
print("Ilość: ", list.count(3)) #ile razy wystepuje 3 w liscie?
print("Index: ", list.index("a")) #na ktorym indexie znajduje się litera a ?
list.remove("b") #usuwa zmienna z listy
print(list)
list2 = [1, 20, 35, -5, 0]
print("Min: ", min(list2))
print("Max: ", max(list2))
list2.sort() #sortuje liste od min
print(list2)
list2.reverse() #odwraca tablice
print(list2)
list2.clear()
print(list2)

print()
print()
print()
i = 0
while i == len(list):
    i += 1
print(list[0])