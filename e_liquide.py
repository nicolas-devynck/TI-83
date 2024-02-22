# from ti_system import *
from math import *
# disp_clr()
print("Calcule Pour e-liquide")
print("----------")
A=input("Arome ML = ? ")
N=input("Taux de nicotine MG/ML = ? ")
if A == "10":
    T=66.7
    # disp_clr()
    print("Resultats")
    print("----------")
    print("Base = "+str(round(T-float(A)-float(N)*3.3, 2))+" ML")
    print("Booster = "+str(float(N)*3.3)+" ML")
    print("Arome = "+str(float(A))+" ML")
elif A == "20":
    T=133.3
    # disp_clr()
    print("Resultats")
    print("----------")
    print("Base = "+str(round(T-float(A)-float(N)*6.6, 2))+" ML")
    print("Booster = "+str(float(N)*6.6)+" ML")
    print("Arome = "+str(float(A))+" ML")
elif A == "30":
    T=200
    # disp_clr()
    print("Resultats")
    print("----------")
    print("Base = "+str(round(T-float(A)-float(N)*10, 2))+" ML")
    print("Booster = "+str(float(N)*10)+" ML")
    print("Arome = "+str(float(A))+" ML")
else:
    print("SVP choisisez un chifre pour l'arome entre : 10, 20 ou 30 ML")

