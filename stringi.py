a1 = " No "
a2 = " Champion name "
a3 = " Rate a champion "

print("*" * len(a1 + a2 + a3) +(8*"*"))
print("||"+ a1 + "|" + "|"+ a2 + "|" + "|"+ a3 + "||")
q = "Y"
while q == "Y":
    q = input("Do you want add a new Champion to the tabel? Choose Y or N: ")
    if q == "Y":
        q1 = input("Choose a champion name: ")
        q2 = input("Choose a rate 0-5: ")
        print("*" * len(a1 + a2 + a3) + (8 * "*"))
        print("||" + a1 + "|" + "|" + a2 + "|" + "|" + a3 + "||")
        print("'" * len(a1 + a2 + a3) +(8*"'"))
        print("|| {:2} || {:13} || {:15} ||" .format(1, q1, q2))
print("Thanks bye bye.")