from ti_system import *
from math import *
disp_clr()
def dec_bin(x:str):
    resultat = ""
    tmp = str(int(fmod(int(x),2)))
    y = int(int(x)/2)
    while (y>0):
        tmp = tmp + str(int(fmod(y,2)))
        y = int(y/2)
    for i in tmp:
        resultat=i+resultat
    return resultat
print(dec_bin(input("x ? ")))