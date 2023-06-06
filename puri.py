# import ti_system import *
# import math import *
import math
# disp_clr()
print("----------")
print("Formule PURI")
print("----------")
P=input("P:Watt = ? ")
U=input("U:Volt = ? ")
R=input("R:Ohm  = ? ")
I=input("I:Ampere = ? ")

# Verification et convertion des input
if P == "":
    P=int(0)
else:
    P=int(P)
if U == "":
    U=int(0)
else:
    U=int(U)
if R == "":
    R=int(0)
else:
    R=int(R)
if I == "":
    I=int(0)
else:
    I=int(I)

# verification qu'il y a au mois 2 valeur
if P==0 and U==0 and R==0:
    # disp_clr()
    print("----------")
    print("Information incorrecte")
    print("----------")
    print("Calcule imposible")
    exit()
if P==0 and U==0 and I==0:
    # disp_clr()
    print("----------")
    print("Information incorrecte")
    print("----------")
    print("Calcule imposible")
    exit()
if P==0 and R==0 and I==0:
    # disp_clr()
    print("----------")
    print("Information incorrecte")
    print("----------")
    print("Calcule imposible")
    exit()
if U==0 and R==0 and I==0:
    # disp_clr()
    print("----------")
    print("Information incorrecte")
    print("----------")
    print("Calcule imposible")
    exit()

# calcule
if P>0 and I>0:
    # disp_clr()
    print("----------")
    print("Resultat")
    print("----------")
    print("P = "+str(P)+" Watt")
    print("U = "+str(P/I)+" Volt")
    print("R = "+str(P/I**2)+" Ohm")
    print("I = "+str(I)+" Ampere")
    exit()
if P>0 and R>0:
    # disp_clr()
    print("----------")
    print("Resultat")
    print("----------")
    print("P = "+str(P)+" Watt")
    print("U = "+str(math.sqrt(P*R))+" Volt")
    print("R = "+str(R)+" Ohm")
    print("I = "+str(math.sqrt(P/R))+" Ampere")
    exit()
if P>0 and U>0:
    # disp_clr()
    print("----------")
    print("Resultat")
    print("----------")
    print("P = "+str(P)+" Watt")
    print("U = "+str(U)+" Volt")
    print("R = "+str(U**2/P)+" Ohm")
    print("I = "+str(P/U)+" Ampere")
    exit()
if I>0 and R>0:
    # disp_clr()
    print("----------")
    print("Resultat")
    print("----------")
    print("P = "+str(R*I**2)+" Watt")
    print("U = "+str(R*I)+" Volt")
    print("R = "+str(R)+" Ohm")
    print("I = "+str(I)+" Ampere")
    exit()
if I>0 and U>0:
    # disp_clr()
    print("----------")
    print("Resultat")
    print("----------")
    print("P = "+str(U*I)+" Watt")
    print("U = "+str(U)+" Volt")
    print("R = "+str(U/I)+" Ohm")
    print("I = "+str(I)+" Ampere")
    exit()
if R>0 and U>0:
    # disp_clr()
    print("----------")
    print("Resultat")
    print("----------")
    print("P = "+str(U**2*R)+" Watt")
    print("U = "+str(U)+" Volt")
    print("R = "+str(R)+" Ohm")
    print("I = "+str(U/R)+" Ampere")
    exit()