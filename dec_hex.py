from ti_system import *
from math import *
disp_clr()
def dec_hex(x:str):
    x = str(x)
    tmp = str(int(fmod(int(x),16)))
    y = int(int(x)/16)
    if tmp == "10":
        tmp = "A"
    elif tmp == "11":
        tmp = "B"
    elif tmp == "12":
        tmp = "C"
    elif tmp == "13":
        tmp = "D"
    elif y == "14":
        tmp = "E"
    elif tmp == "15":
        tmp = "F"
    while (y>0):
        if str(int(fmod(int(y),16))) == "10":
            tmp = tmp + "A"
        elif str(int(fmod(int(y),16))) == "11":
            tmp = tmp + "B"
        elif str(int(fmod(int(y),16))) == "12":
            tmp = tmp + "C"
        elif str(int(fmod(int(y),16))) == "13":
            tmp = tmp + "D"
        elif str(int(fmod(int(y),16))) == "14":
            tmp = tmp + "E"
        elif str(int(fmod(int(y),16))) == "15":
            tmp = tmp + "F"
        else:
            tmp = tmp + str(int(fmod(int(y),16)))
        y = int(int(y/16))
    resultat=""
    for i in tmp:
        resultat=i+resultat
    return resultat
print(dec_hex(input("x ? ")))