#setup
from math import *
from ti_system import *
# fonction watt
def watt_ur():
    disp_clr()
    print("P=U²/R")
    print("----------")
    u = int(input("U ? "))
    r = int(input("R ? "))
    return u**2/r
def watt_ui():
    disp_clr()
    print("P=U*I")
    print("----------")
    u = int(input("U ? "))
    i = int(input("I ? "))
    return u*i
def watt_ri():
    disp_clr()
    print("P=R*I²")
    print("----------")
    r = int(input("R ? "))
    i = int(input("I ? "))
    return r*i**2
# fonction volt
def volt_pr():
    disp_clr()
    print("U=sqrt(P*R)")
    print("----------")
    p = int(input("P ? "))
    r = int(input("R ? "))
    return sqrt(p*r)
def volt_pi():
    disp_clr()
    print("U=P/I")
    print("----------")
    p = int(input("p ? "))
    i = int(input("I ? "))
    return p/i
def volt_ri():
    disp_clr()
    print("U=R*I")
    print("----------")
    r = int(input("R ? "))
    i = int(input("I ? "))
    return r*i
# fonction ohm
def ohm_up():
    disp_clr()
    print("R=U²/P")
    print("----------")
    u = int(input("U ? "))
    p = int(input("P ? "))
    return u**2/p
def ohm_pi():
    disp_clr()
    print("R=P/I²")
    print("----------")
    p = int(input("P ? "))
    i = int(input("I ? "))
    return p/i**2
def ohm_ui():
    disp_clr()
    print("R=U/I")
    print("----------")
    u = int(input("U ? "))
    i = int(input("I ? "))
    return u/i
# fonction amper
def amper_pu():
    disp_clr()
    print("I=P/U")
    print("----------")
    p = int(input("P ? "))
    u = int(input("U ? "))
    return p/u
def amper_ur():
    disp_clr()
    print("I=U/R")
    print("----------")
    u = int(input("U ? "))
    r = int(input("R ? "))
    return u/r
def amper_pr():
    disp_clr()
    print("I=sqrt(P/R)")
    print("----------")
    p = int(input("P ? "))
    r = int(input("R ? "))
    return sqrt(p/r)
#fonction P.U.R.I
def puri():
    #Liste des menus
    menu_0 = ["Exit","Watt = P","Volt = U","Ohm = R","Amper = I"]
    menu_watt = ["Exit","P=U²/R","P=U*I","P=R*I²"]
    menu_volt = ["Exit","U=sqrt(P*R)","U=P/I","U=R*I"]
    menu_ohm = ["Exit","R=U²/P","R=P/I²","R=U/I"]
    menu_amper = ["Exit","I=P/U","I=U/R","I=sqrt(P/R)"]
    disp_clr()
    print("Loi d'ohm")
    print("----------")
    for i in menu_0:
        print(str(menu_0.index(i))+'. '+i)
    in_0 = input("Sélectionnez votre choix ? ")
    if in_0 == "0":
        disp_clr()
    elif in_0 == "1":
        disp_clr()
        print("Watt = P")
        print("----------")
        for i in menu_watt:
            print(str(menu_watt.index(i))+'. '+i)
        in_watt = input("Sélectionnez votre choix ? ")
        if in_watt =="0":
            disp_clr()
        elif in_watt == "1":
            print("Watt (P) = "+str(watt_ur()))
        elif in_watt == "2":
            print("Watt (P) = "+str(watt_ui()))
        elif in_watt == "3":
            print("Watt (P) = "+str(watt_ri()))
        else:
            disp_clr()
            print("Choix non valide") 
    elif in_0 == "2":
        disp_clr()
        print("Volt = U")
        print("----------")
        for i in menu_volt:
            print(str(menu_volt.index(i))+'. '+i)
        in_volt = input("Sélectionnez votre choix ? ")
        if in_volt =="0":
            disp_clr()
        elif in_volt == "1":
            print("Volt (U) = "+str(volt_pr()))
        elif in_volt == "2":
            print("Volt (U) = "+str(volt_pi()))
        elif in_volt == "3":
            print("Volt (U) = "+str(volt_ri()))
        else:
            disp_clr()
            print("Choix non valide") 
    elif in_0 == "3":
        disp_clr()
        print("Ohm = R")
        print("----------")
        for i in menu_ohm:
            print(str(menu_ohm.index(i))+'. '+i)
        in_ohm = input("Sélectionnez votre choix ? ")
        if in_ohm =="0":
            disp_clr()
        elif in_ohm == "1":
            print("Ohm (R) = "+str(ohm_up()))
        elif in_ohm == "2":
            print("Ohm (R) = "+str(ohm_pi()))
        elif in_ohm == "3":
            print("Ohm (R) = "+str(ohm_ui()))
        else:
            disp_clr()
            print("Choix non valide") 
    elif in_0 == "4":
        disp_clr()
        print("Amper = I")
        print("----------")
        for i in menu_amper:
            print(str(menu_amper.index(i))+'. '+i)
        in_amper = input("Sélectionnez votre choix ? ")
        if in_amper =="0":
            disp_clr()
        elif in_amper == "1":
            print("Amper (I) = "+str(amper_pu()))
        elif in_amper == "2":
            print("Amper (I) = "+str(amper_ur()))
        elif in_amper == "3":
            print("Amper (I) = "+str(amper_pr()))
        else:
            disp_clr()
            print("Choix non valide") 
    else:
        disp_clr()
        print("Choix non valide") 
puri()