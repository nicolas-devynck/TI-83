# a modifier pour la TI
import os 
def cls():
    os.system('clear')
# a modifier pour la TI

menu_0 = ["Exit","Watt = P","Volt = U","Ohm = R","Amper = I"]
menu_1 = ["Exit","P=U²/R","P=U*I","P=R*I²"]
menu_2 = ["Exit","U=√P*R","U=P/I","U=R*I"]
menu_3 = ["Exit","R=U²/P","R=P/I²","R=U/I"]
menu_4 = ["Exit","I=P/U","I=U/R","I=√P/R"]
cls()
print("Loi d'ohm")
print("----------")
for i in menu_0:
    print(str(menu_0.index(i))+'. '+i)
in_0 = input("Qu'est-ce que tu aimerais faire ? ")
if in_0 == "0":
    cls()
    print("Goodbye")
elif in_0 == "1":
    cls()
    print("Watt = P")
    print("----------")
    for i in menu_1:
        print(str(menu_1.index(i))+'. '+i)
    in_1 = input("Qu'est-ce que tu aimerais faire ? ")
    if in_1 == "0":
        cls()
        print("Goodbye")
    elif in_1 == "1":
        cls()
        u = int(input("U ? "))
        r = int(input("R ? "))
        print("Watt (P) : "+str(u**2/r))
elif in_0 == "2":
    cls()
    print("Volt = U")
    print("----------")
    for i in menu_2:
        print(str(menu_2.index(i))+'. '+i)
    in_2 = input("Qu'est-ce que tu aimerais faire ? ")
elif in_0 == "3":
    cls()
    print("Ohm = R")
    print("----------")
    for i in menu_3:
        print(str(menu_3.index(i))+'. '+i)
    in_3 = input("Qu'est-ce que tu aimerais faire ? ")
elif in_0 == "4":
    cls()
    print("Amper = I")
    print("----------")
    for i in menu_4:
        print(str(menu_4.index(i))+'. '+i)
    in_4 = input("Qu'est-ce que tu aimerais faire ? ")
elif in_0 != "":
    cls()
    print("Choix non valide Réessayer") 