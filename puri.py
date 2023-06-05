import math
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
# todo
if P>0 and U>0 and R>0:
    print("Calcule imposible ")

# todo calcul selont les valeur fournis
if P>0 and I>0:
    print("R = "+str(P/I**2)+" Ohm")
    print("U = "+str(P/I)+" Volt")
if P>0 and R>0:
    print("I = "+str(sqrt(P/R))+" Ampere")
    print("U = "+str(sqrt(P*R))+" Volt")