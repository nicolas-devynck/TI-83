import math
def hex_dec(x):
    resultat = int(0)
    k = int(1)
    for i in x:
        if i == "A" or i == "a":
            i = "10"
        elif i == "B" or i == "b":
            i = "11"
        elif i == "C" or i == "c":
            i = "12"
        elif i == "D" or i == "d":
            i = "13"
        elif i == "E" or i == "e":
            i = "14"
        elif i == "F" or i == "f":
            i = "15"
        resultat = resultat + int(i)*16**int(len(x)-k)
        k = k+1
    return resultat
print(hex_dec(x = input("x ? ")))